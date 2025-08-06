from django.shortcuts import render
from django.http import JsonResponse
from .models import Reg20222024, Provinsi, Regency, Countries
from django.db.models import Count, Sum, Case, When, IntegerField, Q

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def api_years(request):
    years = [
        {"value": "8", "label": "2022_2023"},
        {"value": "9", "label": "2023_2024"}
    ]
    return JsonResponse({"years": years})

def api_provinces(request):
    provinces = Provinsi.objects.all().values('id', 'name')
    return JsonResponse({"provinces": list(provinces)})

def api_regencies(request):
    province_id = request.GET.get('province_id')
    regencies = Regency.objects.filter(province_id=province_id).values('id', 'name')
    return JsonResponse({"regencies": list(regencies)})

def api_data_national(request):
    year = request.GET.get('year')
    province_id = request.GET.get('province_id')
    regency_id = request.GET.get('regency_id')

    filters = Q(idacademicyeardata=year)
    if province_id:
        filters &= Q(iddataprovinces=province_id)
    if regency_id:
        filters &= Q(iddataregencies=regency_id)

    data = Reg20222024.objects.filter(filters)

    # Statistik
    total_registrants = data.count()
    total_paid = data.filter(ispaid=1).count()

    total_enrolled = data.filter(
        ispaid=1,
        isloapublish=1,
        iswithdrawn=0,
        is_withdrawn=0
    ).count()

    enrollment_rate = round((total_enrolled / total_paid * 100), 2) if total_paid > 0 else 0

    # Peta: agregasi per provinsi/kota
    map_data = []
    if not province_id:
        prov_data = data.values('iddataprovinces').annotate(
            count=Count('idregistrantdata')
        ).order_by('-count')

        for item in prov_data:
            prov = Provinsi.objects.filter(id=item['iddataprovinces']).first()
            if prov:
                map_data.append({
                    "hc-key": f"id-{str(item['iddataprovinces']).zfill(2)}",
                    "value": item['count'],
                    "name": prov.name
                })
    else:
        reg_data = data.values('iddataregencies').annotate(
            count=Count('idregistrantdata')
        )
        for item in reg_data:
            reg = Regency.objects.filter(id=item['iddataregencies']).first()
            if reg:
                map_data.append({
                    "hc-key": f"id-{str(reg.province.id).zfill(2)}-{reg.name.lower().replace(' ', '-')}",
                    "value": item['count'],
                    "name": reg.name
                })

    return JsonResponse({
        "statistics": {
            "total_registrants": total_registrants,
            "total_paid": total_paid,
            "total_enrolled": total_enrolled,
            "enrollment_rate": enrollment_rate
        },
        "map_data": map_data
    })

def api_data_international(request):
    year = request.GET.get('year')
    filters = Q(idacademicyeardata=year)

    data = Reg20222024.objects.filter(filters).exclude(nationality=62)

    total = data.count()
    paid = data.filter(ispaid=1).count()

    # Map data: berdasarkan nationality
    country_data = data.values('nationality').annotate(
        count=Count('idregistrantdata')
    ).order_by('-count')

    map_data = []
    top_countries = []

    for item in country_data:
        country = Countries.objects.filter(idcountrydata=item['nationality']).first()
        iso_code = country.countrycode if country else None
        country_name = country.countryname if country else "Unknown"
        if iso_code:
            map_data.append({
                "code": iso_code,
                "value": item['count']
            })
            top_countries.append({
                "country": country_name,
                "count": item['count']
            })

    # Ambil top 15
    top_countries = top_countries[:15]

    return JsonResponse({
        "statistics": {
            "total": total,
            "paid": paid
        },
        "map_data": map_data,
        "top_countries": top_countries
    })