# apps/administration/urls.py
from django.urls import path
from .views import system_log_view, view_dataset_content

app_name = 'administration'

urlpatterns = [
    path('logs/', system_log_view, name='logs'),
    # URL untuk melihat isi dataset
    path('view/<int:pk>/', view_dataset_content, name='view_dataset'),
]
