# apps/dashboard/models.py

from django.db import models

class Provinsi(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'provinsi'
        verbose_name_plural = 'Provinsi'

    def __str__(self):
        return self.name

class Regency(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.ForeignKey(Provinsi, models.DO_NOTHING, db_column='province_id')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'regency'
        verbose_name_plural = 'Regencies'

    def __str__(self):
        return self.name

class Countries(models.Model):
    idcountrydata = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=2, blank=True, null=True)
    countryname = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)  # Ditambahkan sesuai skema

    class Meta:
        managed = False
        db_table = 'countries'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.countryname or ''

class Eda20232024(models.Model):
    idregistrantdata = models.IntegerField(primary_key=True)
    groupreg = models.CharField(max_length=255, blank=True, null=True)
    asalsekolah = models.CharField(max_length=255, blank=True, null=True)
    graduationyear = models.IntegerField(blank=True, null=True)
    iddataprovinces = models.ForeignKey(Provinsi, models.DO_NOTHING, db_column='iddataprovinces', blank=True, null=True)
    iddataregencies = models.ForeignKey(Regency, models.DO_NOTHING, db_column='iddataregencies', blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)  # Diubah dari CharField ke IntegerField karena di DB sebagai foreign key
    finalscore = models.FloatField(blank=True, null=True)
    ispaid = models.IntegerField(blank=True, null=True)
    isenrolled = models.IntegerField(blank=True, null=True)
    paymentamount = models.IntegerField(blank=True, null=True)  # Ditambahkan sesuai kebutuhan

    class Meta:
        managed = False
        db_table = 'eda_2023_2024'
        verbose_name = 'Data Pendaftar 2023/2024'
        verbose_name_plural = 'Data Pendaftar 2023/2024'

class Eda20222023(models.Model):
    idregistrantdata = models.IntegerField(primary_key=True)
    groupreg = models.CharField(max_length=255, blank=True, null=True)
    asalsekolah = models.CharField(max_length=255, blank=True, null=True)
    graduationyear = models.IntegerField(blank=True, null=True)
    iddataprovinces = models.ForeignKey(Provinsi, models.DO_NOTHING, db_column='iddataprovinces', blank=True, null=True)
    iddataregencies = models.ForeignKey(Regency, models.DO_NOTHING, db_column='iddataregencies', blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)  # Diubah dari CharField ke IntegerField
    finalscore = models.FloatField(blank=True, null=True)
    ispaid = models.IntegerField(blank=True, null=True)
    isenrolled = models.IntegerField(blank=True, null=True)
    paymentamount = models.IntegerField(blank=True, null=True)  # Ditambahkan sesuai kebutuhan

    class Meta:
        managed = False
        db_table = 'eda_2022_2023'
        verbose_name = 'Data Pendaftar 2022/2023'
        verbose_name_plural = 'Data Pendaftar 2022/2023'