# apps/core/admin.py

from django.contrib import admin

class SuperuserAdminSite(admin.AdminSite):
    """
    Custom admin site yang hanya bisa diakses oleh superuser.
    """
    def has_permission(self, request):
        # Kembalikan True jika user aktif dan adalah superuser
        return request.user.is_active and request.user.is_superuser

# Buat instance dari admin site kustom kita
superuser_admin_site = SuperuserAdminSite(name='superuser_admin')
