# apps/dashboard/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from .models import Eda20232024, Eda20222023, Provinsi, Regency, Countries

@login_required
def dashboard_view(request):
    """
    Merender halaman utama dashboard.
    """
    return render(request, 'dashboard/dashboard.html')

@login_required
def api_get_years(request):
    """
    Menyediakan daftar tahun ajaran yang tersedia untuk filter.
    """
    years = [{'value': '2022-2023', 'label': '2022/2023'}, 
             {'value': '2023-2024', 'label': '2023/2024'}]
    return JsonResponse({'years': years})

@login_required
def api_get_provinces(request):
    """
    Mengambil daftar semua provinsi dari database.
    """
    provinces = list(Provinsi.objects.all().order_by('name').values('id', 'name'))
    return JsonResponse({'provinces': provinces})

@login_required
def api_get_regencies(request):
    """
    Mengambil daftar kota/kabupaten berdasarkan ID provinsi yang dipilih.
    """
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse({'regencies': []})
    regencies = list(Regency.objects.filter(province_id=province_id).order_by('name').values('id', 'name'))
    return JsonResponse({'regencies': regencies})

@login_required
def api_get_national_data(request):
    """
    Mengambil dan mengagregasi data pendaftar nasional berdasarkan filter.
    """
    year = request.GET.get('year', '2023-2024')
    province_id = request.GET.get('province_id')
    regency_id = request.GET.get('regency_id')
    
    # Memilih model data berdasarkan tahun yang dipilih
    DataModel = Eda20232024 if year == '2023-2024' else Eda20222023
    
    # Queryset dasar - mengambil SEMUA pendaftar untuk tahun yang dipilih
    # Filter nationality=105 dihapus agar total pendaftar sesuai dengan jumlah semua row
    queryset = DataModel.objects.all()
    
    # Menerapkan filter provinsi dan kota/kabupaten jika ada
    if province_id:
        queryset = queryset.filter(iddataprovinces=province_id)
    if regency_id:
        queryset = queryset.filter(iddataregencies=regency_id)

    # Menghitung statistik utama menggunakan agregasi
    stats_agg = queryset.aggregate(
        total_registrants=Count('idregistrantdata'),
        total_paid=Count('idregistrantdata', filter=Q(ispaid=1)),
        # LOGIKA DIPERBARUI: Menggunakan paymentamount >= 2500000 untuk enroll
        total_enrolled=Count('idregistrantdata', filter=Q(ispaid=1, paymentamount__gte=2500000)),
        total_payment=Sum('paymentamount', filter=Q(ispaid=1))
    )

    # Menghitung tingkat enroll dengan penanganan pembagian nol
    try:
        enrollment_rate = round((stats_agg['total_enrolled'] / stats_agg['total_paid']) * 100, 1)
    except (TypeError, ZeroDivisionError):
        enrollment_rate = 0.0
        
    # Menyusun data statistik untuk dikirim ke frontend
    statistics = {
        'total_registrants': stats_agg['total_registrants'] or 0,
        'total_paid': stats_agg['total_paid'] or 0,
        'total_enrolled': stats_agg['total_enrolled'] or 0,
        'enrollment_rate': enrollment_rate,
        'total_payment': stats_agg['total_payment'] or 0
    }

    # Menyiapkan data untuk visualisasi dan tabel berdasarkan level filter
    visualization = {'type': 'none'}
    table_data = {'headers': [], 'rows': []}

    if regency_id:
        # Level sekolah: tampilkan data per sekolah jika kota/kabupaten dipilih
        school_data = list(queryset.values('asalsekolah')
                               .annotate(
                                   pendaftar=Count('idregistrantdata'),
                                   bayar=Count('idregistrantdata', filter=Q(ispaid=1)),
                                   # LOGIKA DIPERBARUI: Menggunakan paymentamount >= 2500000 untuk enroll
                                   enroll=Count('idregistrantdata', filter=Q(ispaid=1, paymentamount__gte=2500000)),
                                   total_bayar=Sum('paymentamount', filter=Q(ispaid=1))
                               ).order_by('-pendaftar').filter(asalsekolah__isnull=False))
        
        table_data = {
            'headers': ['Asal Sekolah', 'Pendaftar', 'Bayar', 'Enroll', 'Total Pembayaran'],
            'rows': [
                [
                    r['asalsekolah'], 
                    r['pendaftar'], 
                    r['bayar'], 
                    r['enroll'],
                    f"Rp{r['total_bayar']:,}" if r['total_bayar'] else '-'
                ] 
                for r in school_data
            ]
        }
        
    elif province_id:
        # Level kota/kabupaten: tampilkan data per kota jika provinsi dipilih
        # Data ini tetap berasal dari queryset yang sudah difilter (jika ada)
        city_data = list(queryset.filter(iddataprovinces__name__isnull=False).values('iddataregencies__name')
                             .annotate(value=Count('idregistrantdata'))
                             .order_by('-value')
                             .filter(iddataregencies__name__isnull=False))
        
        table_data = {
            'headers': ['Kota/Kabupaten', 'Jumlah Pendaftar'],
            'rows': [[r['iddataregencies__name'], r['value']] for r in city_data]
        }
        
        visualization = {
            'type': 'pie',
            'data': [{'name': r['iddataregencies__name'], 'value': r['value']} for r in city_data]
        }
        
    else:
        # Level provinsi (nasional): tampilkan data per provinsi
        # Data ini tetap berasal dari queryset yang sudah difilter (jika ada)
        province_data = list(queryset.filter(iddataprovinces__name__isnull=False).values('iddataprovinces__name')
                               .annotate(value=Count('idregistrantdata'))
                               .order_by('-value')
                               .filter(iddataprovinces__name__isnull=False))
        
        table_data = {
            'headers': ['Provinsi', 'Jumlah Pendaftar'],
            'rows': [[r['iddataprovinces__name'], r['value']] for r in province_data]
        }
        
        visualization = {
            'type': 'bar',
            'data': [{'name': r['iddataprovinces__name'], 'value': r['value']} for r in province_data[:10]]
        }
    
    return JsonResponse({
        'statistics': statistics,
        'visualization': visualization,
        'table_data': table_data
    })

@login_required
def api_get_international_data(request):
    """
    Mengambil dan mengagregasi data pendaftar internasional.
    """
    year = request.GET.get('year', '2023-2024')
    DataModel = Eda20232024 if year == '2023-2024' else Eda20222023
    
    # Mengambil data selain dari Indonesia dan yang tidak punya data kewarganegaraan
    queryset = DataModel.objects.exclude(Q(nationality=105) | Q(nationality__isnull=True))
    
    # Menghitung jumlah pendaftar per negara
    country_counts = list(queryset.values('nationality')
                               .annotate(value=Count('idregistrantdata'))
                               .order_by('-value'))
    
    # Mengambil informasi detail negara (nama, kode)
    country_lookup = {c.idcountrydata: {'name': c.countryname, 'code': c.countrycode} 
                     for c in Countries.objects.all()}
    
    # Mempersiapkan data untuk tabel dan peta
    table_rows, map_data = [], []
    for row in country_counts:
        cid = row['nationality']
        info = country_lookup.get(cid)
        if info:
            table_rows.append([info['name'], row['value']])
            if info['code']:
                map_data.append({
                    'code': info['code'], 
                    'value': row['value'],
                    'name': info['name']
                })

    return JsonResponse({
        'visualization': {
            'type': 'map',
            'data': map_data
        },
        'table_data': {
            'headers': ['Negara', 'Jumlah Pendaftar'],
            'rows': table_rows
        }
    })
