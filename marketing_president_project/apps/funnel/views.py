# apps/funnel/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.dashboard.models import Provinsi, Regency
import json
import os
from django.conf import settings

@login_required
def funnel_enrollment_view(request):
    """ Menampilkan halaman Funnel Enrollment. """
    provinces = Provinsi.objects.all().order_by('name')
    context = {'provinces': provinces}
    return render(request, 'funnel/funnel_enrollment.html', context)

@login_required
def api_get_funnel_data(request):
    """ API untuk menyediakan data agregat untuk pie chart funnel dan tabel prediksi. """
    province_id = request.GET.get('province_id')
    
    province_json_path = os.path.join(settings.BASE_DIR, 'apps', 'funnel', 'ml_files', 'insight_province_agg.json')
    regency_json_path = os.path.join(settings.BASE_DIR, 'apps', 'funnel', 'ml_files', 'insight_regency_agg.json')

    try:
        with open(province_json_path, 'r') as f:
            province_insights = json.load(f)
        with open(regency_json_path, 'r') as f:
            regency_insights = json.load(f)
    except FileNotFoundError as e:
        return JsonResponse({'error': f'File insight tidak ditemukan: {e.filename}'}, status=500)

    # Inisialisasi variabel total
    total_pendaftar, total_bayar, total_enroll = 0, 0, 0
    table_rows = []
    table_headers = []
    
    provinces = Provinsi.objects.all()
    province_lookup = {str(p.id): p.name for p in provinces}

    if province_id:
        # --- Agregasi data untuk satu provinsi yang dipilih ---
        regencies_in_province = Regency.objects.filter(province_id=province_id)
        table_headers = ['Kota/Kabupaten', 'Pendaftar Aktual', 'Prediksi', 'Bayar Aktual', 'Prediksi', 'Enroll Aktual', 'Prediksi']

        for regency in regencies_in_province:
            regency_key = f"{regency.id}.0"
            insight = regency_insights.get(regency_key)
            if insight:
                # Akumulasi total untuk pie chart
                total_pendaftar += insight.get('total_pendaftar', 0)
                total_bayar += insight.get('total_pembayar', 0)
                total_enroll += insight.get('total_enroll', 0)
                
                # Siapkan baris untuk tabel prediksi
                table_rows.append([
                    regency.name,
                    insight.get('total_pendaftar', 0),
                    round(insight.get('pred_pendaftar', 0)),
                    insight.get('total_pembayar', 0),
                    round(insight.get('pred_bayar', 0)),
                    insight.get('total_enroll', 0),
                    round(insight.get('pred_enroll', 0)),
                ])
    else:
        # --- Agregasi data untuk seluruh provinsi ---
        table_headers = ['Provinsi', 'Pendaftar Aktual', 'Prediksi', 'Bayar Aktual', 'Prediksi', 'Enroll Aktual', 'Prediksi']
        for province_key, insight in province_insights.items():
            clean_key = province_key.split('.')[0]
            province_name = province_lookup.get(clean_key)
            
            if province_name:
                # Akumulasi total untuk pie chart
                total_pendaftar += insight.get('total_pendaftar', 0)
                total_bayar += insight.get('total_pembayar', 0)
                total_enroll += insight.get('total_enroll', 0)
                
                # Siapkan baris untuk tabel prediksi
                table_rows.append([
                    province_name,
                    insight.get('total_pendaftar', 0),
                    round(insight.get('pred_pendaftar', 0)),
                    insight.get('total_pembayar', 0),
                    round(insight.get('pred_bayar', 0)),
                    insight.get('total_enroll', 0),
                    round(insight.get('pred_enroll', 0)),
                ])

    # --- Hitung segmen untuk pie chart ---
    sudah_enroll = total_enroll
    bayar_belum_enroll = max(0, total_bayar - total_enroll)
    daftar_belum_bayar = max(0, total_pendaftar - total_bayar)

    visualization_data = {
        'type': 'pie',
        'labels': ['Daftar (Belum Bayar)', 'Bayar (Belum Enroll)', 'Sudah Enroll'],
        'data': [daftar_belum_bayar, bayar_belum_enroll, sudah_enroll]
    }
    
    summary_data = {
        'total_pendaftar': total_pendaftar,
        'total_bayar': total_bayar,
        'total_enroll': total_enroll
    }
    
    table_data = {
        'headers': table_headers,
        'rows': table_rows
    }

    return JsonResponse({
        'visualization': visualization_data,
        'summary': summary_data,
        'table_data': table_data
    })
