# apps/dashboard/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from .models import Eda20232024, Eda20222023, Provinsi, Regency

# -------------------------------------------------
# VIEW UTAMA UNTUK MENAMPILKAN HALAMAN DASHBOARD
# -------------------------------------------------
@login_required
def dashboard_view(request):
    """
    Hanya me-render template HTML utama. 
    Semua data akan dimuat secara dinamis melalui API.
    """
    return render(request, 'dashboard/dashboard.html')

# -------------------------------------------------
# API VIEWS UNTUK MENYEDIAKAN DATA KE JAVASCRIPT
# -------------------------------------------------

@login_required
def api_get_years(request):
    """ API: Mendapatkan daftar tahun data yang tersedia. """
    years = [
        {'value': '2022-2023', 'label': '2022/2023'},
        {'value': '2023-2024', 'label': '2023/2024'}
    ]
    return JsonResponse({'years': years})

@login_required
def api_get_provinces(request):
    """ API: Mendapatkan daftar provinsi. """
    provinces = list(Provinsi.objects.all().order_by('name').values('id', 'name'))
    return JsonResponse({'provinces': provinces})

@login_required
def api_get_regencies(request):
    """ API: Mendapatkan daftar kota/kabupaten berdasarkan provinsi. """
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse({'regencies': []})
    regencies = list(Regency.objects.filter(province_id=province_id).order_by('name').values('id', 'name'))
    return JsonResponse({'regencies': regencies})

@login_required
def api_get_national_data(request):
    """ API: Mengambil semua data untuk tab Nasional. """
    year = request.GET.get('year', '2023-2024')
    province_id = request.GET.get('province_id')
    regency_id = request.GET.get('regency_id')
    
    DataModel = Eda20232024 if year == '2023-2024' else Eda20222023
    
    queryset = DataModel.objects.filter(nationality='INDONESIA')
    if province_id:
        queryset = queryset.filter(iddataprovinces=province_id)
    if regency_id:
        queryset = queryset.filter(iddataregencies=regency_id)

    # --- Statistics ---
    stats_agg = queryset.aggregate(
        total_registrants=Count('idregistrantdata'),
        total_paid=Count('idregistrantdata', filter=Q(ispaid=1)),
        total_enrolled=Count('idregistrantdata', filter=Q(isenrolled=1))
    )
    enrollment_rate = 0
    if stats_agg['total_paid'] > 0:
        enrollment_rate = round((stats_agg['total_enrolled'] / stats_agg['total_paid']) * 100, 1)

    statistics = {
        'total_registrants': stats_agg['total_registrants'],
        'total_paid': stats_agg['total_paid'],
        'total_enrolled': stats_agg['total_enrolled'],
        'enrollment_rate': enrollment_rate
    }

    # --- Visualization & Table Data ---
    visualization = {}
    table_data = {}

    if regency_id:
        # Level Sekolah
        school_data = list(queryset.values('asalsekolah')
                                   .annotate(pendaftar=Count('idregistrantdata'),
                                             bayar=Count('idregistrantdata', filter=Q(ispaid=1)),
                                             enroll=Count('idregistrantdata', filter=Q(isenrolled=1)))
                                   .order_by('-pendaftar').filter(asalsekolah__isnull=False))
        table_data = {'headers': ['Asal Sekolah', 'Pendaftar', 'Bayar', 'Enroll'], 'rows': [[row['asalsekolah'], row['pendaftar'], row['bayar'], row['enroll']] for row in school_data]}
        visualization = {'type': 'none', 'data': []}

    elif province_id:
        # Level Kota
        city_data = list(queryset.values('iddataregencies__name')
                                 .annotate(value=Count('idregistrantdata'))
                                 .order_by('-value').filter(iddataregencies__name__isnull=False))
        table_data = {'headers': ['Kota/Kabupaten', 'Jumlah Pendaftar'], 'rows': [[row['iddataregencies__name'], row['value']] for row in city_data]}
        visualization = {'type': 'pie', 'data': [{'name': row['iddataregencies__name'], 'value': row['value']} for row in city_data]}

    else:
        # Level Provinsi
        province_data = list(queryset.values('iddataprovinces__name')
                                     .annotate(value=Count('idregistrantdata'))
                                     .order_by('-value').filter(iddataprovinces__name__isnull=False))
        table_data = {'headers': ['Provinsi', 'Jumlah Pendaftar'], 'rows': [[row['iddataprovinces__name'], row['value']] for row in province_data]}
        top_10 = province_data[:10]
        visualization = {'type': 'bar', 'data': [{'name': row['iddataprovinces__name'], 'value': row['value']} for row in top_10]}
    
    return JsonResponse({
        'statistics': statistics,
        'visualization': visualization,
        'table_data': table_data,
    })

@login_required
def api_get_international_data(request):
    """ API: Mengambil semua data untuk tab Internasional. """
    year = request.GET.get('year', '2023-2024')
    DataModel = Eda20232024 if year == '2023-2024' else Eda20222023
    
    queryset = DataModel.objects.exclude(Q(nationality='INDONESIA') | Q(nationality__isnull=True))
    
    country_data = list(queryset.values('nationality')
                                .annotate(value=Count('idregistrantdata'))
                                .order_by('-value'))
    
    table_data = {'headers': ['Negara', 'Jumlah Pendaftar'], 'rows': [[row['nationality'], row['value']] for row in country_data]}
    top_15 = country_data[:15]
    visualization = {'type': 'bar', 'data': [{'name': row['nationality'], 'value': row['value']} for row in top_15]}

    return JsonResponse({
        'visualization': visualization,
        'table_data': table_data,
    })
