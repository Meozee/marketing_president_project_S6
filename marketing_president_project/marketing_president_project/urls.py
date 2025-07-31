# marketing_president_project/urls.py

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Import admin site kustom kita
from apps.core.admin import superuser_admin_site

urlpatterns = [
    path('admin/', superuser_admin_site.urls),
    
    path('auth/', include('apps.users.urls')),
    path('administration/', include('apps.administration.urls')),
    # Tambahkan path untuk aplikasi core
    path('', include('apps.core.urls')),
    path('', include('apps.dashboard.urls')), # Dashboard tetap di root
    path('', include('apps.funnel.urls')), # Tambahkan baris ini
    path('', include('apps.testing.urls')),
    path('testing2/', include('apps.testing2.urls')),# Tambahkan baris ini
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
