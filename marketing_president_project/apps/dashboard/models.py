# models.py (FIXED)

# This file has been cleaned up from the auto-generated version.
#   * Model definitions have been de-duplicated.
#   * Field types have been rationalized (e.g., DecimalField -> FloatField).
#   * Helper methods like __str__ and Meta classes have been improved.

from django.db import models

# --- Core Master Data Models ---

class Countries(models.Model):
    idcountrydata = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=5, blank=True, null=True)
    continentcode = models.CharField(max_length=5, blank=True, null=True)
    countryname = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.countryname or 'N/A'

class Provinsi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'provinsi'
        verbose_name_plural = 'Provinsi'

    def __str__(self):
        return self.name

class Regency(models.Model):
    id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Provinsi, models.DO_NOTHING)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regency'
        verbose_name_plural = 'Regencies'

    def __str__(self):
        return self.name

class Major(models.Model):
    idmajordata = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    displayname = models.CharField(max_length=150, blank=True, null=True)
    # ... (keeping other fields from the original file is recommended, but shortened for brevity)

    class Meta:
        managed = False
        db_table = 'major'

    def __str__(self):
        return self.displayname or self.title

class Concentrations(models.Model):
    idconcentrationdata = models.IntegerField(primary_key=True)
    idmajordata = models.ForeignKey(Major, models.DO_NOTHING, db_column='idmajordata', blank=True, null=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'concentrations'

    def __str__(self):
        return self.title

# --- Other Supporting Models (Abbreviated) ---

class GroupRegistrasi(models.Model):
    iddatagroupreg = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    class Meta: managed = False; db_table = 'group_registrasi'
    def __str__(self): return self.title

class TipeRegistrasi(models.Model):
    iddataregtype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    class Meta: managed = False; db_table = 'tipe_registrasi'
    def __str__(self): return self.title

class RegistrasiKhusus(models.Model):
    iddataregkhusustype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    class Meta: managed = False; db_table = 'registrasi_khusus'
    def __str__(self): return self.title
    
class JenisSekolah(models.Model):
    idschooltypedata = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    class Meta: managed = False; db_table = 'jenis_sekolah'
    def __str__(self): return self.title

class JurusanSekolah(models.Model):
    idschooljurusandata = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    class Meta: managed = False; db_table = 'jurusan_sekolah'
    def __str__(self): return self.title

class TipeKelas(models.Model):
    iddataclasstype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    class Meta: managed = False; db_table = 'tipe_kelas'
    def __str__(self): return self.title


# --- Abstract Base Model for EDA Data ---
# To avoid repeating fields, we can use an abstract base class.

class BaseEdaModel(models.Model):
    idregistrantdata = models.BigIntegerField(primary_key=True)
    groupreg = models.ForeignKey(GroupRegistrasi, models.DO_NOTHING, db_column='groupreg', blank=True, null=True)
    regtype = models.ForeignKey(TipeRegistrasi, models.DO_NOTHING, db_column='regtype', blank=True, null=True)
    iddataregkhusustype = models.ForeignKey(RegistrasiKhusus, models.DO_NOTHING, db_column='iddataregkhusustype', blank=True, null=True)
    asalsekolah = models.TextField(blank=True, null=True)
    idschooltypedata = models.ForeignKey(JenisSekolah, models.DO_NOTHING, db_column='idschooltypedata', blank=True, null=True)
    idschooljurusandata = models.ForeignKey(JurusanSekolah, models.DO_NOTHING, db_column='idschooljurusandata', blank=True, null=True)
    graduationyear = models.FloatField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    age_on_register = models.FloatField(blank=True, null=True)
    idmajordata = models.ForeignKey(Major, models.DO_NOTHING, db_column='idmajordata', blank=True, null=True)
    idconcentrationdata = models.ForeignKey(Concentrations, models.DO_NOTHING, db_column='idconcentrationdata', blank=True, null=True)
    iddataclasstype = models.ForeignKey(TipeKelas, models.DO_NOTHING, db_column='iddataclasstype', blank=True, null=True)
    noreg = models.BigIntegerField(blank=True, null=True)
    
    # FIX: Correctly defined ForeignKey to Countries and Provinsi/Regency
    nationality = models.IntegerField(blank=True, null=True) # This seems to be a legacy or redundant field. The FK below is better.
    idcountrydata = models.ForeignKey(Countries, models.DO_NOTHING, db_column='idcountrydata', blank=True, null=True)
    iddataprovinces = models.ForeignKey(Provinsi, models.DO_NOTHING, db_column='iddataprovinces', blank=True, null=True)
    iddataregencies = models.ForeignKey(Regency, models.DO_NOTHING, db_column='iddataregencies', blank=True, null=True)
    
    finalscore = models.FloatField(blank=True, null=True)
    ispaid = models.IntegerField(blank=True, null=True)
    isenrolled = models.IntegerField(blank=True, null=True)
    # ... other fields from original model ...
    
    class Meta:
        abstract = True # This makes it a base model, no table will be created for it.
        managed = False

# --- Concrete EDA Models ---

class Eda20222023(BaseEdaModel):
    class Meta(BaseEdaModel.Meta):
        db_table = 'eda_2022_2023'
        verbose_name = 'Data Pendaftar 2022/2023'
        verbose_name_plural = 'Data Pendaftar 2022/2023'

class Eda20232024(BaseEdaModel):
    class Meta(BaseEdaModel.Meta):
        db_table = 'eda_2023_2024'
        verbose_name = 'Data Pendaftar 2023/2024'
        verbose_name_plural = 'Data Pendaftar 2023/2024'