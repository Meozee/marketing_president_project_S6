# apps/testing/views.py
from django.shortcuts import render
from .utils import load_model, clean_dataframe
import json
import random
import os
import pandas as pd
from django.conf import settings
from .models import (
    GroupReg, jenis_sekolah, jurusan_sekolah, major,
    concentrations, countries, provinsi, regency,
    registrasi_khusus, tipe_kelas, tipe_registrasi
)

def testing_home(request):
    return render(request, 'testing/testing.html')

def handle_csv_upload(request):
    if request.method == "POST" and request.FILES.get('datasetFile'):
        file = request.FILES['datasetFile']
        df = pd.read_csv(file)
        
        # Ambil kolom yang diperlukan
        with open(os.path.join(settings.BASE_DIR, 'apps', 'testing', 'model', 'columns_used.json')) as f:
            used_columns = json.load(f)

        # Pastikan hanya pakai kolom yang sesuai
        df = clean_dataframe(df, used_columns)

        try:
            model_bayar = load_model('model_bayar.joblib')
            model_enroll = load_model('model_enroll.joblib')
            model_pendaftar = load_model('model_pendaftar.joblib')
        except Exception as e:
            return render(request, 'testing/testing.html', {
                'error': f"Gagal memuat model: {e}"
            })

        # Prediksi
        try:
            # df['pred_bayar'] = model_bayar.predict(df).sum()
            # df['pred_enroll'] = model_enroll.predict(df).sum()
            # df['pred_pendaftar'] = model_pendaftar.predict(df).sum()
            # yang ini gunainnya
            pred_bayar = model_bayar.predict(df).sum()
            pred_enroll = model_enroll.predict(df).sum()
            pred_pendaftar = model_pendaftar.predict(df).sum()

        except Exception as e:
            return render(request, 'testing/testing.html', {
                'error': f"Gagal melakukan prediksi: {e}"
            })

        return render(request, 'testing/testing.html', {
            'pred_bayar': int(pred_bayar),
            'pred_enroll': int(pred_enroll),
            'pred_pendaftar': int(pred_pendaftar),
            'description': request.POST.get('description', 'Hasil Prediksi')
        })


    return render(request, 'testing/testing.html')

def handle_form_predict(request):
    if request.method == "POST":
        # Load kolom yang digunakan
        with open(os.path.join(settings.BASE_DIR, 'apps', 'testing', 'model', 'columns_used.json')) as f:
            used_columns = json.load(f)

        # Ambil data default (5 baris)
        default_df = pd.read_csv(os.path.join(settings.BASE_DIR, 'apps', 'testing', 'data', 'data_default.csv'))
        default_df = default_df[used_columns]

        # Ambil input user
        form_data = {key: request.POST.get(key, "") for key in used_columns}
        user_row = pd.DataFrame([form_data])
        user_row = clean_dataframe(user_row, used_columns)

        # Ganti 1 baris di default dengan data user (acak 1 indeks)
        replace_idx = random.choice(default_df.index)
        default_df.loc[replace_idx] = user_row.iloc[0]

        # Bersihkan data akhir
        df_final = clean_dataframe(default_df, used_columns)

        # Load model
        try:
            model_bayar = load_model('model_bayar.joblib')
            model_enroll = load_model('model_enroll.joblib')
            model_pendaftar = load_model('model_pendaftar.joblib')
        except Exception as e:
            return render(request, 'testing/testing.html', {'error': f"Gagal memuat model: {e}"})

        # Prediksi
        try:
            pred_bayar = int(model_bayar.predict(df_final).sum())
            pred_enroll = int(model_enroll.predict(df_final).sum())
            pred_pendaftar = int(model_pendaftar.predict(df_final).sum())
        except Exception as e:
            return render(request, 'testing/testing.html', {'error': f"Gagal melakukan prediksi: {e}"})

        return render(request, 'testing/testing.html', {
            'pred_bayar': pred_bayar,
            'pred_enroll': pred_enroll,
            'pred_pendaftar': pred_pendaftar
        })

    return render(request, 'testing/testing.html')

def testing_home(request):
    context = {
        'groupreg_choices': GroupReg.objects.all(),
        'jenis_sekolah_choices': jenis_sekolah.objects.all(),
        'jurusan_sekolah_choices': jurusan_sekolah.objects.all(),
        'major_choices': major.objects.all(),
        'concentration_choices': concentrations.objects.all(),
        'country_choices': countries.objects.all(),
        'province_choices': provinsi.objects.all(),
        'regency_choices': regency.objects.all(),
        'registrasi_khusus_choices': registrasi_khusus.objects.all(),
        'tipe_kelas_choices': tipe_kelas.objects.all(),
        'tipe_registrasi_choices': tipe_registrasi.objects.all(),
    }

    return render(request, 'testing/testing.html', context)