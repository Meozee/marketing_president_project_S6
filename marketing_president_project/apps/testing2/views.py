import os
import pandas as pd
import joblib
import json
import numpy as np
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from apps.testing.models import provinsi, major, regency, countries

MODEL_FILES_DIR = os.path.join(settings.BASE_DIR, 'apps', 'testing2', 'model')
preprocessor_path = os.path.join(MODEL_FILES_DIR, 'preprocessor.pkl')
model_pendaftar_path = os.path.join(MODEL_FILES_DIR, 'model_pendaftar.pkl')
model_bayar_path = os.path.join(MODEL_FILES_DIR, 'model_bayar.pkl')
model_enroll_path = os.path.join(MODEL_FILES_DIR, 'model_enroll.pkl')
columns_used_path = os.path.join(MODEL_FILES_DIR, 'columns_used.json')


MODEL_DIR = os.path.join(settings.BASE_DIR, 'apps', 'testing2', 'model')

# Create your views here.
def testing_view(request):
    provinces = provinsi.objects.all()
    majors = major.objects.all()
    countries_list = countries.objects.all()
    regencies = regency.objects.all()
    dataset_ready = bool(request.session.get('latest_df'))

    return render(request, 'testing2/testing2.html', {
        'provinces': provinces,
        'majors': majors,
        'countries': countries_list,
        'regencies': regencies,
        'dataset_ready': dataset_ready, 
    })

def upload_csv(request):
    if request.method == 'POST':
        simulate_only = request.POST.get('simulate_only')  # tombol simulasi ditekan
        description = request.POST.get('description')
        sim_finalscore = request.POST.get('sim_finalscore')
        sim_idtipelulusanprofexe = request.POST.get('sim_idtipelulusanprofexe')

        # Jika mode simulasi, ambil dari session
        if simulate_only:
            df_json = request.session.get('latest_df')
            if not df_json:
                messages.error(request, "Tidak ada data sebelumnya untuk disimulasikan.")
                return redirect('testing2:testing2')
            df = pd.read_json(df_json)
        else:
            # Mode upload file baru
            csv_file = request.FILES.get('datasetFile')
            if not csv_file:
                messages.error(request, 'Silakan unggah file CSV terlebih dahulu.')
                return redirect('testing2:testing2')
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File harus berformat .csv')
                return redirect('testing2:testing2')
            
            try:
                df = pd.read_csv(csv_file)
            except Exception as e:
                messages.error(request, f"Gagal membaca file CSV: {e}")
                return redirect('testing2:testing2')

            request.session['latest_df'] = df.to_json()

        try:
            # Load model dan preprocessor
            print("📦 Loading model dan preprocessor")
            preprocessor = joblib.load(preprocessor_path)
            model_pendaftar = joblib.load(model_pendaftar_path)
            model_bayar = joblib.load(model_bayar_path)
            model_enroll = joblib.load(model_enroll_path)

            importance_df = get_feature_importance(model_bayar, preprocessor)
            print(importance_df.head(10))

            with open(columns_used_path, 'r') as f:
                expected_columns = json.load(f)

            missing = [col for col in expected_columns if col not in df.columns]
            if missing:
                return HttpResponse(f"❌ CSV kurang kolom: {missing}", status=400)

            for col in expected_columns:
                if col not in df.columns:
                    df[col] = pd.NA

            if 'dob' in df.columns:
                df = df.drop(columns=['dob'])

            df = df.loc[:, ~df.columns.duplicated()]
            for col in ['idcountrydata', 'iddataprovinces', 'iddataregencies', 'asalsekolah']:
                if col in df.columns:
                    df[col] = df[col].astype(str)

            df.replace({'t': 1, 'f': 0}, inplace=True)

            # Terapkan simulasi
            if sim_finalscore in ['0', '1']:
                df['finalscore'] = int(sim_finalscore)
            if sim_idtipelulusanprofexe in ['0', '1', '2', '3']:
                df['idtipelulusanprofexe'] = int(sim_idtipelulusanprofexe)

            print("🔄 Transforming data")
            X_processed = preprocessor.transform(df)

            pred_pendaftar = model_pendaftar.predict(X_processed)
            pred_bayar = model_bayar.predict(X_processed)

            pred_enroll = np.zeros_like(pred_bayar)
            paid_indices = np.where(pred_bayar >= 0.09)[0]

            if len(paid_indices) > 0:
                pred_enroll_paid = model_enroll.predict(X_processed[paid_indices])
                pred_enroll[paid_indices] = pred_enroll_paid
            else:
                print("⚠️ Tidak ada data dengan prediksi bayar == 1")
                
            # Simpan versi mentah (belum diprediksi)
            request.session['raw_df'] = df.to_json()    
                
            # Simpan hasil prediksi ke dalam df
            df['pred_pendaftar'] = pred_pendaftar
            df['pred_bayar'] = pred_bayar
            df['pred_enroll'] = pred_enroll
                
            # Simpan ke session
            request.session['latest_df'] = df.to_json()

            result = {
                'desc': description,
                'pendaftar': int(pred_pendaftar.sum()),
                'bayar': int(pred_bayar.sum()),
                'enroll': int(pred_enroll.sum()),
            }

            return render(request, 'testing2/testing2.html', {
                    'result': result,
                    'provinces': provinsi.objects.all(),
                    'majors': major.objects.all(),
                    'countries': countries.objects.filter(idcountrydata__in=[105, 999]),  # Batasi
                    'regencies': regency.objects.all(),
                    'dataset_ready': True,  # ⬅️ flag ini kuncinya
            })

        except Exception as e:
            print("❌ Terjadi error:", e)
            messages.error(request, f"Gagal memproses data: {e}")
            return redirect('testing2:testing2')


def get_feature_importance(model, preprocessor):
    feature_names = preprocessor.get_feature_names_out()
    importances = model.feature_importances_

    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    })
    
    return importance_df.sort_values(by='importance', ascending=False)


def filter_prediksi(request):
    if request.method != 'POST':
        return redirect('testing2:testing2')

    df_json = request.session.get('raw_df')
    if not df_json:
        messages.error(request, "Tidak ada data untuk difilter.")
        return redirect('testing2:testing2')

    try:
        # Load dataframe
        df = pd.read_json(df_json)
        df = df.loc[:, ~df.columns.duplicated()]  # hapus kolom duplikat

        # Ambil input
        country = request.POST.get('country')
        prov = request.POST.get('provinsi')
        regency_val = request.POST.get('regency')

        if prov:
            prov = str(int(float(prov))).strip()
        if regency_val:
            regency_val = str(int(float(regency_val))).strip()

        print("🧾 Form input:")
        print(" - country:", country)
        print(" - provinsi:", prov)
        print(" - regency :", regency_val)

        # Cleaning kolom ID agar aman dan rapi
        for col in ['idcountrydata', 'iddataprovinces', 'iddataregencies', 'asalsekolah']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')  # ubah ke int, NaN jika gagal
                df[col] = df[col].astype('Int64').astype(str).str.strip()

        # Filter negara
        if country:
            df = df[df['idcountrydata'] == str(country)]
            print("✅ Setelah filter country:", df.shape)

        # Filter Indonesia berdasarkan provinsi dan kabupaten
        if country == '105':  # Indonesia
            if prov:
                match_prov = df['iddataprovinces'] == prov
                print(f"🔍 Match provinsi? {match_prov.any()} ({prov})")
                df = df[match_prov]
                print("✅ Setelah filter provinsi:", df.shape)
                
            # Validasi jika regency dipilih tapi tidak ditemukan dalam provinsi
            if regency_val:
                available_regencies = df['iddataregencies'].dropna().unique().tolist()
                if regency_val not in available_regencies:
                    # Ambil nama-nama kabupaten yang valid dalam provinsi yang dipilih
                    regency_objects = regency.objects.filter(id__in=available_regencies)
                    regency_names = [f"{r.id} - {r.name}" for r in regency_objects]

                    messages.warning(request, f"Tidak ditemukan data untuk kabupaten/kota ID {regency_val} di provinsi yang dipilih.")

                    return render(request, 'testing2/testing2.html', {
                        'result': None,
                        'table': None,
                        'provinces': provinsi.objects.all(),
                        'majors': major.objects.all(),
                        'countries': countries.objects.filter(idcountrydata__in=[105, 999]),
                        'regencies': regency.objects.all(),
                        'dataset_ready': True,
                        'regency_info': regency_names,  # tambahkan ini ke template jika mau ditampilkan
                    })

            if regency_val:
                match_reg = df['iddataregencies'] == regency_val
                print(f"🔍 Match regency? {match_reg.any()} ({regency_val})")
                df = df[match_reg]
                print("✅ Setelah filter regency:", df.shape)

        # Debug isi kolom
        print("🧪 Unique idcountrydata:", df['idcountrydata'].unique())
        print("🧪 Unique provinces:", df['iddataprovinces'].unique())
        print("🧪 Unique regencies:", df['iddataregencies'].unique())

        # Validasi data kosong
        if df.empty:
            messages.warning(request, "Hasil filter kosong. Tidak ada data yang bisa diprediksi.")
            return render(request, 'testing2/testing2.html', {
                'result': None,
                'table': None,
                'provinces': provinsi.objects.all(),
                'majors': major.objects.all(),
                'countries': countries.objects.filter(idcountrydata__in=[105, 999]),
                'regencies': regency.objects.all(),
                'dataset_ready': True,
            })

        # Load model & preprocessor
        preprocessor = joblib.load(preprocessor_path)
        model_pendaftar = joblib.load(model_pendaftar_path)
        model_bayar = joblib.load(model_bayar_path)
        model_enroll = joblib.load(model_enroll_path)

        # Replace nilai boolean jika perlu
        df.replace({'t': 1, 'f': 0}, inplace=True)

        # Prediksi
        X_processed = preprocessor.transform(df)
        pred_pendaftar = model_pendaftar.predict(X_processed)
        pred_bayar = model_bayar.predict(X_processed)

        pred_enroll = np.zeros_like(pred_bayar)
        paid_indices = np.where(pred_bayar >= 0.09)[0]
        if len(paid_indices) > 0:
            pred_enroll_paid = model_enroll.predict(X_processed[paid_indices])
            pred_enroll[paid_indices] = pred_enroll_paid

        df['pendaftar'] = pred_pendaftar
        df['pembayar'] = pred_bayar
        df['enroll'] = pred_enroll

        # Grup data berdasarkan kolom yang sesuai
        group_col = (
            'asalsekolah' if regency_val else
            'iddataregencies' if prov else
            'iddataprovinces' if country == '105' else
            'idcountrydata'
        )

        table = None
        if group_col and group_col in df.columns:
            table = (
                df.groupby(group_col)[['pendaftar', 'pembayar', 'enroll']]
                .sum()
                .reset_index()
                .rename(columns={group_col: 'group_col'})
            )

            # Mapping ID ke nama
            if group_col == 'idcountrydata':
                id_map = {str(c.idcountrydata): c.countryname for c in countries.objects.all()}
                table['group_col'] = table['group_col'].astype(float).astype(int).astype(str)
                table['group_col'] = table['group_col'].map(id_map)
                table.rename(columns={'group_col': 'Negara'}, inplace=True)
            elif group_col == 'iddataprovinces':
                id_map = {str(p.id): p.name for p in provinsi.objects.all()}
                table['group_col'] = table['group_col'].astype(float).astype(int).astype(str)
                table['group_col'] = table['group_col'].map(id_map)
                table.rename(columns={'group_col': 'Provinsi'}, inplace=True)
            elif group_col == 'iddataregencies':
                id_map = {str(r.id): r.name for r in regency.objects.all()}
                table['group_col'] = table['group_col'].astype(float).astype(int).astype(str)
                table['group_col'] = table['group_col'].map(id_map)
                table.rename(columns={'group_col': 'Kabupaten/Kota'}, inplace=True)
            elif group_col == 'asalsekolah':
                table.rename(columns={'group_col': 'Asal Sekolah'}, inplace=True)

            table['total_enroll'] = table['pembayar'] + table['enroll']

        result = {
            'pendaftar': int(df['pendaftar'].sum()),
            'bayar': int(df['pembayar'].sum()),
            'enroll': int(df['enroll'].sum()),
        }

        print("📊 Dataframe final preview:")
        print(df[['idcountrydata', 'iddataprovinces', 'iddataregencies', 'asalsekolah']].head())

        return render(request, 'testing2/testing2.html', {
            'result': result,
            'table': table.to_dict(orient='records') if table is not None else None,
            'provinces': provinsi.objects.all(),
            'majors': major.objects.all(),
            'countries': countries.objects.filter(idcountrydata__in=[105, 999]),
            'regencies': regency.objects.all(),
            'dataset_ready': True,
        })

    except Exception as e:
        print("❌ Terjadi error di filter_prediksi:", e)
        messages.error(request, f"Gagal memproses data: {e}")
        return redirect('testing2:testing2')
