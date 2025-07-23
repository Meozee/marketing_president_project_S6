# apps/dashboard/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Eda20232024, Provinsi  # Pastikan model ini sudah ada
import json

@login_required
def home_view(request):
    """
    View untuk menampilkan halaman utama/beranda.
    """
    context = {
        'user': request.user
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def dashboard_view(request):
    """
    View untuk menampilkan dashboard visualisasi utama.
    """
    # Query untuk menghitung jumlah pendaftar per provinsi
    # Kita menggunakan 'iddataprovinces' dari tabel eda_2023_2024
    # dan menghubungkannya dengan tabel 'provinsi'
    provinsi_data = (
        Eda20232024.objects
        .filter(iddataprovinces__isnull=False) # Hanya ambil data yang provinsinya terisi
        .values('iddataprovinces') # Group by provinsi ID
        .annotate(total=Count('iddataprovinces')) # Hitung jumlah pendaftar
        .order_by('-total') # Urutkan dari yang terbanyak
    )

    # Ambil nama provinsi dari tabel Provinsi
    provinsi_map = {p.id: p.name for p in Provinsi.objects.all()}

    # Siapkan data untuk chart
    labels = []
    data = []
    for item in provinsi_data:
        # Cocokkan id provinsi dengan namanya
        provinsi_name = provinsi_map.get(item['iddataprovinces'])
        if provinsi_name:
            labels.append(provinsi_name)
            data.append(item['total'])

    context = {
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
    }

    return render(request, 'dashboard/dashboard.html', context)


@login_required
def dashboard_view(request):
    """
    View untuk menampilkan dashboard visualisasi utama,
    sekarang dengan logika filter.
    """
    # Ambil ID provinsi yang dipilih dari URL (GET parameter)
    selected_province_id = request.GET.get('provinsi', None)

    # Ambil semua provinsi untuk ditampilkan di dropdown filter
    all_provinces = Provinsi.objects.all().order_by('name')

    chart_title = "Jumlah Pendaftar per Provinsi"
    labels = []
    data = []

    if selected_province_id and selected_province_id.isdigit():
        # --- JIKA PROVINSI DIPILIH ---
        selected_province_id = int(selected_province_id)
        selected_province = Provinsi.objects.get(id=selected_province_id)
        chart_title = f"Jumlah Pendaftar per Kabupaten/Kota di {selected_province.name.title()}"

        # Query data per kabupaten/kota di provinsi yang dipilih
        regency_data = (
            Eda20232024.objects
            .filter(iddataprovinces=selected_province_id)
            .values('iddataregencies')
            .annotate(total=Count('iddataregencies'))
            .order_by('-total')
        )
        
        regency_map = {r.id: r.name for r in Regency.objects.filter(province_id=selected_province_id)}
        
        for item in regency_data:
            regency_name = regency_map.get(item['iddataregencies'])
            if regency_name:
                labels.append(regency_name.title())
                data.append(item['total'])

    else:
        # --- JIKA TIDAK ADA PROVINSI YANG DIPILIH (TAMPILAN NASIONAL) ---
        provinsi_data = (
            Eda20232024.objects
            .filter(iddataprovinces__isnull=False)
            .values('iddataprovinces')
            .annotate(total=Count('iddataprovinces'))
            .order_by('-total')
        )
        provinsi_map = {p.id: p.name for p in all_provinces}
        for item in provinsi_data:
            provinsi_name = provinsi_map.get(item['iddataprovinces'])
            if provinsi_name:
                labels.append(provinsi_name.title())
                data.append(item['total'])

    context = {
        'chart_title': chart_title,
        'chart_labels': json.dumps(labels),
        'chart_data': json.dumps(data),
        'all_provinces': all_provinces,
        'selected_province_id': selected_province_id,
    }

    return render(request, 'dashboard/dashboard.html', context)
