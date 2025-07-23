# views.py (FIXED)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
# FIX: Import all necessary models
from .models import Eda20232024, Eda20222023, Provinsi, Regency, Countries
import json

# ... (dashboard_view, get_available_years, get_provinces, get_regencies remain the same) ...
@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def get_available_years(request):
    years = [
        {'value': '2022-2023', 'label': '2022/2023'},
        {'value': '2023-2024', 'label': '2023/2024'}
    ]
    return JsonResponse({'years': years})

@login_required
def get_provinces(request):
    provinces = list(Provinsi.objects.all().order_by('name').values('id', 'name'))
    return JsonResponse({'provinces': provinces})

@login_required
def get_regencies(request):
    province_id = request.GET.get('province_id')
    if not province_id:
        return JsonResponse({'regencies': []})
    regencies = list(Regency.objects.filter(province_id=province_id).order_by('name').values('id', 'name'))
    return JsonResponse({'regencies': regencies})


@login_required
def get_dashboard_data(request):
    """
    API endpoint utama untuk mengambil semua data dashboard yang dibutuhkan.
    """
    year = request.GET.get('year', '2023-2024')
    data_type = request.GET.get('type', 'national')
    
    DataModel = Eda20232024 if year == '2023-2024' else Eda20222023
    
    response_data = {}

    if data_type == 'national':
        province_id = request.GET.get('province_id')
        regency_id = request.GET.get('regency_id')

        # FIX: Filter by country name via ForeignKey, not the incorrect integer field
        queryset = DataModel.objects.filter(idcountrydata__countryname='INDONESIA')
        
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

        response_data['statistics'] = {
            'total_registrants': stats_agg['total_registrants'],
            'total_paid': stats_agg['total_paid'],
            'total_enrolled': stats_agg['total_enrolled'],
            'enrollment_rate': enrollment_rate
        }

        # --- Visualization & Table Data ---
        if regency_id:
            # Level Sekolah
            table_rows = list(queryset.values('asalsekolah')
                                      .annotate(pendaftar=Count('idregistrantdata'),
                                                bayar=Count('idregistrantdata', filter=Q(ispaid=1)),
                                                enroll=Count('idregistrantdata', filter=Q(isenrolled=1)))
                                      .order_by('-pendaftar').filter(asalsekolah__isnull=False)[:50]) # Add limit for performance
            response_data['table_data'] = {
                'headers': ['Asal Sekolah', 'Pendaftar', 'Bayar', 'Enroll'],
                'rows': [[row['asalsekolah'], row['pendaftar'], row['bayar'], row['enroll']] for row in table_rows]
            }
            response_data['visualization'] = {'type': 'none', 'data': []}

        elif province_id:
            # Level Kota
            city_data = list(queryset.values('iddataregencies__name')
                                     .annotate(value=Count('idregistrantdata'))
                                     .order_by('-value').filter(iddataregencies__name__isnull=False))
            response_data['table_data'] = {
                'headers': ['Kota/Kabupaten', 'Jumlah Pendaftar'],
                'rows': [[row['iddataregencies__name'], row['value']] for row in city_data]
            }
            response_data['visualization'] = {
                'type': 'pie', # Changed from 'regencies' to 'pie' to match JS
                'data': [{'name': row['iddataregencies__name'], 'value': row['value']} for row in city_data]
            }

        else:
            # Level Provinsi
            province_data = list(queryset.values('iddataprovinces__name')
                                         .annotate(value=Count('idregistrantdata'))
                                         .order_by('-value').filter(iddataprovinces__name__isnull=False))
            response_data['table_data'] = {
                'headers': ['Provinsi', 'Jumlah Pendaftar'],
                'rows': [[row['iddataprovinces__name'], row['value']] for row in province_data]
            }
            top_10 = province_data[:10]
            response_data['visualization'] = {
                'type': 'bar',
                'data': [{'name': row['iddataprovinces__name'], 'value': row['value']} for row in top_10]
            }
    
    elif data_type == 'international':
        # FIX: Exclude by country name via ForeignKey and handle nulls correctly
        queryset = DataModel.objects.exclude(
            Q(idcountrydata__countryname='INDONESIA') | Q(idcountrydata__isnull=True)
        )
        
        stats_agg = queryset.aggregate(
            total_registrants=Count('idregistrantdata'),
            total_paid=Count('idregistrantdata', filter=Q(ispaid=1)),
            total_enrolled=Count('idregistrantdata', filter=Q(isenrolled=1))
        )
        enrollment_rate = 0
        if stats_agg['total_paid'] > 0:
            enrollment_rate = round((stats_agg['total_enrolled'] / stats_agg['total_paid']) * 100, 1)

        response_data['statistics'] = {
            'total_registrants': stats_agg['total_registrants'],
            'total_paid': stats_agg['total_paid'],
            'total_enrolled': stats_agg['total_enrolled'],
            'enrollment_rate': enrollment_rate
        }

        # FIX: Group by country name from the related table
        country_data = list(queryset.values('idcountrydata__countryname')
                                    .annotate(value=Count('idregistrantdata'))
                                    .order_by('-value').filter(idcountrydata__countryname__isnull=False))
        
        # FIX: Use the correct field name 'idcountrydata__countryname'
        response_data['table_data'] = {
            'headers': ['Negara', 'Jumlah Pendaftar'],
            'rows': [[row['idcountrydata__countryname'], row['value']] for row in country_data]
        }
        top_15 = country_data[:15]
        response_data['visualization'] = {
            'type': 'bar',
            'data': [{'name': row['idcountrydata__countryname'], 'value': row['value']} for row in top_15]
        }

    return JsonResponse(response_data)