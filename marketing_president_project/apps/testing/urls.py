# testing/urls.py
from django.urls import path
from .views import testing_home, handle_csv_upload, handle_form_predict

app_name = 'testing'

urlpatterns = [
    path('', testing_home, name='testing'),
    path('testing/', testing_home, name='testing'),
    path('upload/', handle_csv_upload, name='upload_csv'),
    path('form/', handle_form_predict, name='form_predict'),
]
