# apps/administration/forms.py

from django import forms
from .models import DatasetUpload

class DatasetUploadForm(forms.ModelForm):
    class Meta:
        model = DatasetUpload
        # Tampilkan field ini saja di form
        fields = ['nama_data', 'file_path']
        widgets = {
            'nama_data': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'file_path': forms.FileInput(attrs={'class': 'block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'}),
        }
        labels = {
            'nama_data': 'Nama/Deskripsi Data',
            'file_path': 'Pilih File Dataset',
        }
