# apps/dashboard/urls.py

from django.urls import path
# Hanya impor fungsi yang ada dan digunakan
from .views import dashboard_view, get_available_years, get_provinces, get_regencies, get_dashboard_data


# app_name membantu membedakan URL antar aplikasi
app_name = 'dashboard'

urlpatterns = [
    # URL untuk halaman utama (beranda)
    path('', home_view, name='home'),
    
    # URL untuk halaman dashboard visualisasi
    path('dashboard/', dashboard_view, name='main_dashboard'),
]
