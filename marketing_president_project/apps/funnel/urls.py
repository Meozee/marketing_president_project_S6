# apps/funnel/urls.py

from django.urls import path
from .views import funnel_enrollment_view, api_get_funnel_data

app_name = 'funnel'

urlpatterns = [
    # URL untuk halaman utama Funnel Enrollment
    path('', funnel_enrollment_view, name='funnel_page'),
    path('funnel-enrollment/', funnel_enrollment_view, name='funnel_page'),
    
    # URL untuk API yang akan dipanggil oleh JavaScript
    path('api/funnel-data/', api_get_funnel_data, name='api_funnel_data'),
]
