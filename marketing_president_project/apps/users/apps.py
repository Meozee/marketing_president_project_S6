# apps/users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    # Fungsi ini WAJIB ada untuk mendaftarkan signals.py
    def ready(self):
        import apps.users.signals
