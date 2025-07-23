from django.db import models

class DataTables(models.Model):
    data = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'data_tables'

class Genders(models.Model):
    gender = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'genders'

class Groups(models.Model):
    groupname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'groups'

class Questions(models.Model):
    question = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'questions'

class Registrants(models.Model):
    fullname = models.TextField(blank=True, null=True)
    gender = models.ForeignKey(Genders, models.DO_NOTHING, blank=True, null=True)
    idnumber = models.TextField(blank=True, null=True)
    school = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    regtype = models.TextField(blank=True, null=True)
    regtime = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'registrants'

class Roles(models.Model):
    role = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'roles'

class Sessions(models.Model):
    session = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sessions'

class Users(models.Model):
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'users'
