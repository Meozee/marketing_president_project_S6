# apps/dashboard/urls.py

from django.urls import path
from .views import home_view, dashboard_view

# app_name membantu membedakan URL antar aplikasi
app_name = 'dashboard'

urlpatterns = [
    # URL untuk halaman utama (beranda)
    path('', home_view, name='home'),
    
    # URL untuk halaman dashboard visualisasi
    path('dashboard/', dashboard_view, name='main_dashboard'),
]
