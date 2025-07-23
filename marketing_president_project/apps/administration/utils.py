# apps/administration/utils.py

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType

def create_log_entry(user, obj, action_flag, message=""):
    """
    Fungsi untuk membuat LogEntry secara manual.
    - user: User yang melakukan aksi.
    - obj: Objek yang dikenai aksi (misal: instance user, instance dataset).
    - action_flag: ADDITION, CHANGE, atau DELETION.
    - message: Pesan custom untuk log.
    """
    LogEntry.objects.create(
        user_id=user.id,
        content_type_id=ContentType.objects.get_for_model(obj).pk,
        object_id=obj.pk,
        object_repr=str(obj),
        action_flag=action_flag,
        change_message=message
    )
