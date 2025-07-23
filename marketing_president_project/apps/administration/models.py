# apps/administration/models.py

from django.db import models
from django.conf import settings

# --- Model dari tabel yang sudah ada (Legacy Database) ---

class Eda20232024(models.Model):
    idregistrantdata = models.IntegerField(primary_key=True)
    
    # PERBAIKAN: Tipe data diubah dari CharField(max_length=-1) menjadi IntegerField
    groupreg = models.IntegerField(blank=True, null=True)
    regtype = models.IntegerField(blank=True, null=True)
    
    # PERBAIKAN: Tipe data diubah dari CharField(max_length=-1) menjadi TextField untuk teks yang panjang
    asalsekolah = models.TextField(blank=True, null=True)
    
    graduationyear = models.IntegerField(blank=True, null=True)
    
    # PERBAIKAN: Tipe data diubah dari CharField(max_length=-1) menjadi IntegerField
    nationality = models.IntegerField(blank=True, null=True)
    
    iddataprovinces = models.IntegerField(blank=True, null=True)
    iddataregencies = models.IntegerField(blank=True, null=True)
    finalscore = models.FloatField(blank=True, null=True)
    
    # PERBAIKAN: Tipe data diubah dari CharField(max_length=-1) menjadi TextField
    rank = models.TextField(blank=True, null=True)
    
    iddatapassingstatus = models.IntegerField(blank=True, null=True)
    ispaid = models.BooleanField(blank=True, null=True)
    isenrolled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False  # Penting karena ini adalah tabel yang sudah ada
        db_table = 'eda_2023_2024'
        verbose_name = 'Data Pendaftar 2023/2024'
        verbose_name_plural = 'Data Pendaftar 2023/2024'

class Provinsi(models.Model):
    # Menggunakan IntegerField untuk primary key jika tipe datanya integer di DB
    id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'provinsi'

    def __str__(self):
        return self.name

# --- Model untuk tabel baru yang akan dibuat Django ---

class DatasetUpload(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    id_data = models.AutoField(primary_key=True)
    nama_data = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='datasets/')
    tanggal_upload = models.DateTimeField(auto_now_add=True)
    tanggal_approve = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='uploaded_files')
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_files')

    class Meta:
        # 'managed = True' adalah default, jadi tidak perlu ditulis
        db_table = 'dataset_upload_history'
        ordering = ['-tanggal_upload']

    def __str__(self):
        return f"{self.nama_data} ({self.get_status_display()})"