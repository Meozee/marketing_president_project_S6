from django.db import models

# Create your models here.

# models.py
class GroupReg(models.Model):
    iddatagroupreg = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'group_registrasi'

    def __str__(self):
        return f"{self.iddatagroupreg} - {self.title}"


class jenis_sekolah(models.Model):
    idschooltypedata = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'jenis_sekolah'

    def __str__(self):
        return f"{self.idschooltypedata} - {self.title}"
    

class jurusan_sekolah(models.Model):
    idschooljurusandata = models.IntegerField(primary_key=True)
    idschooltypedata = models.ForeignKey('jenis_sekolah', on_delete=models.DO_NOTHING, db_column='idschooltypedata')
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'jurusan_sekolah'

    def __str__(self):
        return f"{self.idschooljurusandata} - {self.title}"
    
    
class major(models.Model):
    idmajordata = models.IntegerField(primary_key=True)
    idfacultydata = models.IntegerField()
    title = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'major'

    def __str__(self):
        return f"{self.idmajordata} - {self.title}"
        
    
class concentrations(models.Model):
    idconcentrationdata = models.IntegerField(primary_key=True)
    idmajordata = models.ForeignKey('major', on_delete=models.DO_NOTHING, db_column='idmajordata')
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'concentrations'

    def __str__(self):
        return f"{self.idconcentrationdata} - {self.title}"
    

class countries(models.Model):
    idcountrydata = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=5)
    continentcode = models.CharField(max_length=5)
    countryname = models.CharField(max_length=100)
    fullname = models.CharField(max_length=150)
    
    class Meta:
        db_table = 'countries'

    def __str__(self):
        return f"{self.idcountrydata} - {self.countryname}"
    

class provinsi(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'provinsi'

    def __str__(self):
        return f"{self.id} - {self.name}"
    

class regency(models.Model):
    id = models.IntegerField(primary_key=True)
    province_id = models.ForeignKey('provinsi', on_delete=models.DO_NOTHING, db_column='province_id')
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'regency'

    def __str__(self):
        return f"{self.id} - {self.name}"

class registrasi_khusus(models.Model):
    iddataregkhusustype  = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'registrasi_khusus'

    def __str__(self):
        return f"{self.iddataregkhusustype } - {self.title}"
    
class tipe_kelas(models.Model):
    iddataclasstype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tipe_kelas'

    def __str__(self):
        return f"{self.iddataclasstype} - {self.title}"
    
    
class tipe_registrasi(models.Model):
    iddataregtype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    displayname = models.CharField(max_length=100)
    reg_displayname = models.CharField(max_length=100)
    groupreg_displayname = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'tipe_registrasi'

    def __str__(self):
        return f"{self.iddataregtype} - {self.title}"