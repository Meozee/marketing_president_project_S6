# apps/users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User

# Import model dan form dari aplikasi lain
from apps.administration.models import DatasetUpload
from apps.administration.forms import DatasetUploadForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Import fungsi log kita dan flag aksi
from apps.administration.utils import create_log_entry
from django.contrib.admin.models import ADDITION, CHANGE, DELETION

# --- FUNGSI LOGIN DAN LOGOUT (TIDAK PERLU LOGGING DI SINI) ---
def login_view(request):
    # ... (kode login_view tetap sama)
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Sinyal akan menangani logging di sini
                return redirect('dashboard:home')
    # ... (sisa kode login_view)
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    # Sinyal akan menangani logging di sini
    logout(request)
    messages.info(request, "Anda telah berhasil logout.")
    return redirect('users:login')

# --- FUNGSI HELPER UNTUK CEK ROLE ---
def is_staff_user(user):
    return user.is_staff

def is_superuser(user):
    return user.is_superuser

# --- VIEW CRUD USER DENGAN LOGGING ---
@login_required
@user_passes_test(is_superuser)
def user_add_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'User baru berhasil ditambahkan.')
            # LOGGING: Catat penambahan user
            create_log_entry(request.user, new_user, ADDITION, "User baru ditambahkan melalui form web.")
            return redirect('users:approvals')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Tambah User Baru'})

@login_required
@user_passes_test(is_superuser)
def user_edit_view(request, pk):
    user_to_edit = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_to_edit)
        if form.is_valid():
            form.save()
            messages.success(request, f'Data user {user_to_edit.username} berhasil diperbarui.')
            # LOGGING: Catat perubahan user
            create_log_entry(request.user, user_to_edit, CHANGE, "Data user diperbarui melalui form web.")
            return redirect('users:approvals')
    else:
        form = CustomUserChangeForm(instance=user_to_edit)
    return render(request, 'users/user_form.html', {'form': form, 'title': f'Edit User: {user_to_edit.username}'})

@login_required
@user_passes_test(is_superuser)
def user_delete_view(request, pk):
    user_to_delete = User.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user == user_to_delete:
            messages.error(request, 'Anda tidak bisa menghapus akun Anda sendiri.')
            return redirect('users:approvals')
        
        # LOGGING: Catat penghapusan user SEBELUM dihapus
        create_log_entry(request.user, user_to_delete, DELETION, f"User '{user_to_delete.username}' dihapus.")
        user_to_delete.delete()
        messages.success(request, f'User {user_to_delete.username} berhasil dihapus.')
        return redirect('users:approvals')
    return render(request, 'users/user_confirm_delete.html', {'user_to_delete': user_to_delete})

# --- registrar_approvals_view DENGAN LOGGING ---
@login_required
@user_passes_test(is_staff_user)
def registrar_approvals_view(request):
    if request.method == 'POST':
        if 'approve_id' in request.POST:
            if request.user.is_superuser:
                dataset = DatasetUpload.objects.get(id_data=request.POST.get('approve_id'))
                dataset.status = 'APPROVED'
                dataset.approver = request.user
                dataset.tanggal_approve = timezone.now()
                dataset.save()
                messages.success(request, f"Dataset '{dataset.nama_data}' telah disetujui.")
                # LOGGING: Catat persetujuan
                create_log_entry(request.user, dataset, CHANGE, f"Menyetujui dataset: {dataset.nama_data}")
            return redirect('users:approvals')

        elif 'reject_id' in request.POST:
            if request.user.is_superuser:
                dataset = DatasetUpload.objects.get(id_data=request.POST.get('reject_id'))
                dataset.status = 'REJECTED'
                dataset.approver = request.user
                dataset.tanggal_approve = timezone.now()
                dataset.save()
                messages.warning(request, f"Dataset '{dataset.nama_data}' telah ditolak.")
                # LOGGING: Catat penolakan
                create_log_entry(request.user, dataset, CHANGE, f"Menolak dataset: {dataset.nama_data}")
            return redirect('users:approvals')
        
        else:
            form = DatasetUploadForm(request.POST, request.FILES)
            if form.is_valid():
                upload_instance = form.save(commit=False)
                upload_instance.uploader = request.user
                upload_instance.save()
                messages.success(request, "Dataset berhasil diunggah dan sedang menunggu persetujuan.")
                # LOGGING: Catat upload
                create_log_entry(request.user, upload_instance, ADDITION, f"Mengunggah dataset baru: {upload_instance.nama_data}")
            else:
                messages.error(request, "Gagal mengunggah dataset. Periksa kembali isian form.")
            return redirect('users:approvals')

    all_users = User.objects.all().order_by('username')
    upload_form = DatasetUploadForm()
    all_uploads = DatasetUpload.objects.all().order_by('-tanggal_upload')
    context = {
        'all_users': all_users,
        'upload_form': upload_form,
        'all_uploads': all_uploads,
    }
    return render(request, 'users/registrar_approvals.html', context)
