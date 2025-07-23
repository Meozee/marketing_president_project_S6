from django.contrib import admin
from .models import (
    DataTables, Genders, Groups, Questions,
    Registrants, Roles, Sessions, Users
)

admin.site.register(DataTables)
admin.site.register(Genders)
admin.site.register(Groups)
admin.site.register(Questions)
admin.site.register(Registrants)
admin.site.register(Roles)
admin.site.register(Sessions)
admin.site.register(Users)
