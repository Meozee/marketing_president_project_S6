# apps/dashboard/urls.py

from django.urls import path
from .views import (
    dashboard_view, 
    api_get_years, 
    api_get_provinces, 
    api_get_regencies, 
    api_get_national_data,
    api_get_international_data
)

app_name = 'dashboard'

urlpatterns = [
    # URL untuk halaman utama dashboard (yang me-render HTML)
    path('', dashboard_view, name='home'), # Menambahkan ini untuk root URL
    path('dashboard/', dashboard_view, name='main_dashboard'),

    # URL untuk API endpoints yang akan dipanggil oleh JavaScript
    path('api/years/', api_get_years, name='api_years'),
    path('api/provinces/', api_get_provinces, name='api_provinces'),
    path('api/regencies/', api_get_regencies, name='api_regencies'),
    path('api/data/national/', api_get_national_data, name='api_data_national'),
    path('api/data/international/', api_get_international_data, name='api_data_international'),
]
