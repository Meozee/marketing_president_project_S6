# apps/administration/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.models import LogEntry
from .models import DatasetUpload
import pandas as pd

# Fungsi helper untuk memeriksa role user
def is_staff_user(user):
    return user.is_staff

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def system_log_view(request):
    """
    View untuk menampilkan log aktivitas sistem.
    """
    logs = LogEntry.objects.all().select_related('user', 'content_type').order_by('-action_time')[:50]
    context = {'logs': logs}
    return render(request, 'administration/system_log.html', context)

# --- FUNGSI YANG HILANG SEBELUMNYA ADA DI SINI ---
@login_required
@user_passes_test(is_staff_user)
def view_dataset_content(request, pk):
    """
    View untuk menampilkan pratinjau isi file dataset (CSV/Excel).
    """
    dataset = get_object_or_404(DatasetUpload, pk=pk)
    html_table = None
    error_message = None

    try:
        # Cek ekstensi file dan baca sesuai jenisnya
        file_path = dataset.file_path.path
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            # Tampilkan 50 baris pertama
            html_table = df.head(50).to_html(classes='min-w-full bg-white', border=0, index=False)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
            # Tampilkan 50 baris pertama
            html_table = df.head(50).to_html(classes='min-w-full bg-white', border=0, index=False)
        else:
            error_message = "Format file tidak didukung untuk pratinjau. Hanya .csv, .xls, .xlsx."
    except Exception as e:
        error_message = f"Gagal membaca file: {e}"

    context = {
        'dataset': dataset,
        'html_table': html_table,
        'error_message': error_message,
    }
    return render(request, 'administration/view_dataset.html', context)
