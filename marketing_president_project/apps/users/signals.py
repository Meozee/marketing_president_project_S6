# apps/users/signals.py

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry, ADDITION, DELETION
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """
    Mencatat setiap kali user berhasil login dengan pesan yang jelas.
    """
    LogEntry.objects.create(
        user_id=user.id,
        content_type_id=ContentType.objects.get_for_model(User).pk,
        object_id=user.pk,
        object_repr=str(user),
        action_flag=ADDITION,
        # Pesan yang lebih deskriptif
        change_message=f"User '{user.username}' telah login."
    )

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    """
    Mencatat setiap kali user logout dengan pesan yang jelas.
    """
    if user:
        LogEntry.objects.create(
            user_id=user.id,
            content_type_id=ContentType.objects.get_for_model(User).pk,
            object_id=user.pk,
            object_repr=str(user),
            action_flag=DELETION,
            # Pesan yang lebih deskriptif
            change_message=f"User '{user.username}' telah logout."
        )
