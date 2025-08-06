from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='home'),
    path('dashboard/', views.dashboard_view, name='main_dashboard'),
    path('api/years/', views.api_years, name='api_years'),
    path('api/provinces/', views.api_provinces, name='api_provinces'),
    path('api/regencies/', views.api_regencies, name='api_regencies'),
    path('api/data/national/', views.api_data_national, name='api_data_national'),
    path('api/data/international/', views.api_data_international, name='api_data_international'),
]
