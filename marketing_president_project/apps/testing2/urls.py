from django.urls import path
from .views import testing_view, upload_csv, filter_prediksi

app_name = 'testing2'

urlpatterns = [
    path('', testing_view, name='testing2'),
    path('upload/', upload_csv, name='upload_csv'),
    path('filter/', filter_prediksi, name='filter_prediksi'),
]