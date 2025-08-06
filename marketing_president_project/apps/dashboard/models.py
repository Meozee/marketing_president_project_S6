from django.db import models

class Provinsi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'provinsi'

class Regency(models.Model):
    id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Provinsi, models.DO_NOTHING)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regency'

class Countries(models.Model):
    idcountrydata = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=5, blank=True, null=True)
    continentcode = models.CharField(max_length=5, blank=True, null=True)
    countryname = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'

class Major(models.Model):
    idmajordata = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major'

class Reg20222024(models.Model):
    idregistrantdata = models.BigIntegerField(blank=True, null=True)
    namalengkap = models.TextField(blank=True, null=True)
    idnumber = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    idmajordata = models.BigIntegerField(blank=True, null=True)
    idcountrydata = models.BigIntegerField(blank=True, null=True)
    iddataprovinces = models.BigIntegerField(blank=True, null=True)
    iddataregencies = models.BigIntegerField(blank=True, null=True)
    nationality = models.BigIntegerField(blank=True, null=True)
    idacademicyeardata = models.BigIntegerField(blank=True, null=True)
    ispaid = models.BigIntegerField(blank=True, null=True)
    isloapublish = models.BigIntegerField(blank=True, null=True)
    iswithdrawn = models.BigIntegerField(blank=True, null=True)
    is_withdrawn = models.BigIntegerField(blank=True, null=True)
    isenrolled = models.BigIntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    dob = models.TextField(blank=True, null=True)
    birthplace = models.TextField(blank=True, null=True)
    alamatrumah = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    kelurahan = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REG2022_2024'