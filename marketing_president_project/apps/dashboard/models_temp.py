# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models






class Concentrations(models.Model):
    idconcentrationdata = models.IntegerField(primary_key=True)
    idmajordata = models.ForeignKey('Major', models.DO_NOTHING, db_column='idmajordata', blank=True, null=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'concentrations'


class Countries(models.Model):
    idcountrydata = models.IntegerField(primary_key=True)
    countrycode = models.CharField(max_length=5, blank=True, null=True)
    continentcode = models.CharField(max_length=5, blank=True, null=True)
    countryname = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class DataTables(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tables'



class Eda20222023(models.Model):
    idregistrantdata = models.BigIntegerField(primary_key=True)
    groupreg = models.ForeignKey('GroupRegistrasi', models.DO_NOTHING, db_column='groupreg', blank=True, null=True)
    regtype = models.ForeignKey('TipeRegistrasi', models.DO_NOTHING, db_column='regtype', blank=True, null=True)
    iddataregkhusustype = models.ForeignKey('RegistrasiKhusus', models.DO_NOTHING, db_column='iddataregkhusustype', blank=True, null=True)
    isregtypechanged = models.IntegerField(blank=True, null=True)
    oldregtype = models.IntegerField(blank=True, null=True)
    regtypechangeby = models.IntegerField(blank=True, null=True)
    is_onlinetest = models.IntegerField(blank=True, null=True)
    is_onlinetest_taken = models.IntegerField(blank=True, null=True)
    qty_onlinetest_taken = models.IntegerField(blank=True, null=True)
    is_tryout = models.IntegerField(blank=True, null=True)
    asalsekolah = models.TextField(blank=True, null=True)
    idschooltypedata = models.ForeignKey('JenisSekolah', models.DO_NOTHING, db_column='idschooltypedata', blank=True, null=True)
    idschooljurusandata = models.ForeignKey('JurusanSekolah', models.DO_NOTHING, db_column='idschooljurusandata', blank=True, null=True)
    graduationyear = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    highschoolcountry = models.IntegerField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    age_on_register = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idmajordata = models.ForeignKey('Major', models.DO_NOTHING, db_column='idmajordata', blank=True, null=True)
    idconcentrationdata = models.ForeignKey(Concentrations, models.DO_NOTHING, db_column='idconcentrationdata', blank=True, null=True)
    idmajordata2_dualdegree = models.IntegerField(blank=True, null=True)
    iddataclasstype = models.ForeignKey('TipeKelas', models.DO_NOTHING, db_column='iddataclasstype', blank=True, null=True)
    ismajorchanged = models.IntegerField(blank=True, null=True)
    oldmajor = models.IntegerField(blank=True, null=True)
    majorchangeby = models.IntegerField(blank=True, null=True)
    noreg = models.BigIntegerField(blank=True, null=True)
    ideventdata = models.IntegerField(blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    idcountrydata = models.ForeignKey(Countries, models.DO_NOTHING, db_column='idcountrydata', blank=True, null=True)
    iddataprovinces = models.ForeignKey('Provinsi', models.DO_NOTHING, db_column='iddataprovinces', blank=True, null=True)
    iddataregencies = models.ForeignKey('Regency', models.DO_NOTHING, db_column='iddataregencies', blank=True, null=True)
    kelurahan = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    intl_country = models.TextField(blank=True, null=True)
    isaddresscheck = models.IntegerField(blank=True, null=True)
    isaddresscheckedby = models.IntegerField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    iddatawhyuniv = models.IntegerField(blank=True, null=True)
    iddatawhymajor = models.IntegerField(blank=True, null=True)
    iddatainfouniv = models.IntegerField(blank=True, null=True)
    puatscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    puetscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    finalscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    isrankchanged = models.IntegerField(blank=True, null=True)
    oldrank = models.TextField(blank=True, null=True)
    rankchangeby = models.IntegerField(blank=True, null=True)
    is_raporautorank = models.IntegerField(blank=True, null=True)
    is_prestasiautorank = models.IntegerField(blank=True, null=True)
    is_utbkautorank = models.IntegerField(blank=True, null=True)
    is_unbkautorank = models.IntegerField(blank=True, null=True)
    iddatatipelulusanprofexe = models.IntegerField(blank=True, null=True)
    iddatapassingstatus = models.IntegerField(blank=True, null=True)
    isrankconfirm = models.IntegerField(blank=True, null=True)
    isrankedby = models.IntegerField(blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    referralwithdrawseq = models.IntegerField(blank=True, null=True)
    iddatawithdrawstatus = models.IntegerField(blank=True, null=True)
    idacademicyeardata = models.IntegerField(blank=True, null=True)
    duplicatesametrack = models.IntegerField(blank=True, null=True)
    duplicatedifftrack = models.IntegerField(blank=True, null=True)
    isloapublish = models.IntegerField(blank=True, null=True)
    idpublishloasessiondata = models.IntegerField(blank=True, null=True)
    isloapublish_onlinetest = models.IntegerField(blank=True, null=True)
    isloaextensionpublish = models.IntegerField(blank=True, null=True)
    is_autoloaextensionpublish = models.IntegerField(blank=True, null=True)
    idpublishloaextensionsessiondata = models.IntegerField(blank=True, null=True)
    is_autoloapublish = models.IntegerField(blank=True, null=True)
    is_autoloapublish_viawa = models.IntegerField(blank=True, null=True)
    dateloapublish = models.DateTimeField(blank=True, null=True)
    isloarepublish = models.IntegerField(blank=True, null=True)
    islatpublish = models.IntegerField(blank=True, null=True)
    is_autolatpublish_viawa = models.IntegerField(blank=True, null=True)
    islat2publish = models.IntegerField(blank=True, null=True)
    islat3publish = models.IntegerField(blank=True, null=True)
    islat4publish = models.IntegerField(blank=True, null=True)
    islcdnpublish = models.IntegerField(blank=True, null=True)
    iddatamedfinalrank = models.IntegerField(blank=True, null=True)
    ispaid = models.IntegerField(blank=True, null=True)
    paymentamount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_forceautoloa_2020 = models.IntegerField(blank=True, null=True)
    iswithdrawn = models.IntegerField(blank=True, null=True)
    withdrawnby = models.IntegerField(blank=True, null=True)
    isenrolled = models.IntegerField(blank=True, null=True)
    israporsubmit = models.IntegerField(blank=True, null=True)
    israporreceivedby = models.IntegerField(blank=True, null=True)
    isprestasisubmit = models.IntegerField(blank=True, null=True)
    isprestasireceivedby = models.IntegerField(blank=True, null=True)
    idtelemarketingdata = models.IntegerField(blank=True, null=True)
    idteleanswerdata = models.IntegerField(blank=True, null=True)
    is_oldmigrated = models.IntegerField(blank=True, null=True)
    is_rgmigrated = models.IntegerField(blank=True, null=True)
    is_rapormigrated = models.IntegerField(blank=True, null=True)
    is_profexemigrated = models.IntegerField(blank=True, null=True)
    is_earlyreg = models.IntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    iddatareligion = models.IntegerField(blank=True, null=True)
    pushprovince = models.IntegerField(blank=True, null=True)
    pushregencies = models.IntegerField(blank=True, null=True)
    ispushupdated = models.IntegerField(blank=True, null=True)
    ismypushupdated = models.IntegerField(blank=True, null=True)
    isassignnomovingin = models.IntegerField(blank=True, null=True)
    issentnomovingin = models.IntegerField(blank=True, null=True)
    isreserveroom = models.IntegerField(blank=True, null=True)
    isassignroomno = models.IntegerField(blank=True, null=True)
    idroomno = models.IntegerField(blank=True, null=True)
    roomno_queue = models.IntegerField(blank=True, null=True)
    needtemproom = models.IntegerField(blank=True, null=True)
    idroomtempno = models.IntegerField(blank=True, null=True)
    planstsnbh = models.TextField(blank=True, null=True)
    getstsnbh = models.TextField(blank=True, null=True)
    changetosingle = models.IntegerField(blank=True, null=True)
    roompriorityno = models.IntegerField(blank=True, null=True)
    assignroomby = models.IntegerField(blank=True, null=True)
    isassignschsib = models.IntegerField(blank=True, null=True)
    schsibby = models.IntegerField(blank=True, null=True)
    isassignschkjbbk = models.IntegerField(blank=True, null=True)
    schkjbbkby = models.IntegerField(blank=True, null=True)
    createvisaby = models.IntegerField(blank=True, null=True)
    is_reg_with_payment = models.IntegerField(blank=True, null=True)
    is_notifpaid_sent = models.IntegerField(blank=True, null=True)
    payment_status = models.TextField(blank=True, null=True)
    payment_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_servicefee = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_trxfee = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_withdrawn = models.IntegerField(blank=True, null=True)
    withdrawseq = models.IntegerField(blank=True, null=True)
    idgradform_rmsdata = models.IntegerField(blank=True, null=True)
    idgradform_tipekerjadata = models.IntegerField(blank=True, null=True)
    idgradform_ispresuniv = models.IntegerField(blank=True, null=True)
    idintlform_admissionterm = models.IntegerField(blank=True, null=True)
    iddatatipeangsuran = models.IntegerField(blank=True, null=True)
    idconcentrationgraduatedata = models.IntegerField(blank=True, null=True)
    is_inquiryresign = models.IntegerField(blank=True, null=True)
    refundpaid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_medicaldata_verified = models.IntegerField(blank=True, null=True)
    med_is_stage1_pass = models.IntegerField(blank=True, null=True)
    med_is_stage2_paid = models.IntegerField(blank=True, null=True)
    med_is_stage2_pass = models.IntegerField(blank=True, null=True)
    med_is_stage3_pass = models.IntegerField(blank=True, null=True)
    datestamp = models.DateTimeField(blank=True, null=True)
    idcreated = models.IntegerField(blank=True, null=True)
    idmodify = models.IntegerField(blank=True, null=True)
    cicilan_terms1amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms1due = models.DateTimeField(blank=True, null=True)
    cicilan_terms2amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms2due = models.DateTimeField(blank=True, null=True)
    cicilan_terms3amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms3due = models.DateTimeField(blank=True, null=True)
    cicilan_terms4amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms4due = models.DateTimeField(blank=True, null=True)
    cicilan_terms5amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms5due = models.DateTimeField(blank=True, null=True)
    cicilan_terms6amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms6due = models.DateTimeField(blank=True, null=True)
    cicilan_terms7amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms7due = models.DateTimeField(blank=True, null=True)
    cicilan_terms8amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms8due = models.DateTimeField(blank=True, null=True)
    idregbranddata = models.IntegerField(blank=True, null=True)
    umur = models.IntegerField(blank=True, null=True)
    age_imputed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms1due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms2due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms3due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms4due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms5due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms6due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms7due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms8due_known = models.IntegerField(blank=True, null=True)
    dateloapublish_known = models.IntegerField(blank=True, null=True)
    total_cicilan = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    assumed_enrolled = models.BooleanField(blank=True, null=True)
    label_bayar = models.IntegerField(blank=True, null=True)
    label_enroll = models.IntegerField(blank=True, null=True)
    finalscore_bin_left = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    finalscore_bin_right = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eda_2022_2023'


class Eda20232024(models.Model):
    idregistrantdata = models.BigIntegerField(primary_key=True)
    groupreg = models.ForeignKey('GroupRegistrasi', models.DO_NOTHING, db_column='groupreg', blank=True, null=True)
    regtype = models.ForeignKey('TipeRegistrasi', models.DO_NOTHING, db_column='regtype', blank=True, null=True)
    iddataregkhusustype = models.ForeignKey('RegistrasiKhusus', models.DO_NOTHING, db_column='iddataregkhusustype', blank=True, null=True)
    isregtypechanged = models.IntegerField(blank=True, null=True)
    oldregtype = models.IntegerField(blank=True, null=True)
    regtypechangeby = models.IntegerField(blank=True, null=True)
    is_onlinetest = models.IntegerField(blank=True, null=True)
    is_onlinetest_taken = models.IntegerField(blank=True, null=True)
    qty_onlinetest_taken = models.IntegerField(blank=True, null=True)
    is_tryout = models.IntegerField(blank=True, null=True)
    asalsekolah = models.TextField(blank=True, null=True)
    idschooltypedata = models.ForeignKey('JenisSekolah', models.DO_NOTHING, db_column='idschooltypedata', blank=True, null=True)
    idschooljurusandata = models.ForeignKey('JurusanSekolah', models.DO_NOTHING, db_column='idschooljurusandata', blank=True, null=True)
    graduationyear = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    highschoolcountry = models.IntegerField(blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    age_on_register = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idmajordata = models.ForeignKey('Major', models.DO_NOTHING, db_column='idmajordata', blank=True, null=True)
    idconcentrationdata = models.ForeignKey(Concentrations, models.DO_NOTHING, db_column='idconcentrationdata', blank=True, null=True)
    idmajordata2_dualdegree = models.IntegerField(blank=True, null=True)
    iddataclasstype = models.ForeignKey('TipeKelas', models.DO_NOTHING, db_column='iddataclasstype', blank=True, null=True)
    ismajorchanged = models.IntegerField(blank=True, null=True)
    oldmajor = models.IntegerField(blank=True, null=True)
    majorchangeby = models.IntegerField(blank=True, null=True)
    noreg = models.BigIntegerField(blank=True, null=True)
    ideventdata = models.IntegerField(blank=True, null=True)
    nationality = models.IntegerField(blank=True, null=True)
    idcountrydata = models.ForeignKey(Countries, models.DO_NOTHING, db_column='idcountrydata', blank=True, null=True)
    iddataprovinces = models.ForeignKey('Provinsi', models.DO_NOTHING, db_column='iddataprovinces', blank=True, null=True)
    iddataregencies = models.ForeignKey('Regency', models.DO_NOTHING, db_column='iddataregencies', blank=True, null=True)
    kelurahan = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    intl_country = models.TextField(blank=True, null=True)
    isaddresscheck = models.IntegerField(blank=True, null=True)
    isaddresscheckedby = models.IntegerField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    iddatawhyuniv = models.IntegerField(blank=True, null=True)
    iddatawhymajor = models.IntegerField(blank=True, null=True)
    iddatainfouniv = models.IntegerField(blank=True, null=True)
    puatscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    puetscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    finalscore = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    isrankchanged = models.IntegerField(blank=True, null=True)
    oldrank = models.TextField(blank=True, null=True)
    rankchangeby = models.IntegerField(blank=True, null=True)
    is_raporautorank = models.IntegerField(blank=True, null=True)
    is_prestasiautorank = models.IntegerField(blank=True, null=True)
    is_utbkautorank = models.IntegerField(blank=True, null=True)
    is_unbkautorank = models.IntegerField(blank=True, null=True)
    iddatatipelulusanprofexe = models.IntegerField(blank=True, null=True)
    iddatapassingstatus = models.IntegerField(blank=True, null=True)
    isrankconfirm = models.IntegerField(blank=True, null=True)
    isrankedby = models.IntegerField(blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    referralwithdrawseq = models.IntegerField(blank=True, null=True)
    iddatawithdrawstatus = models.IntegerField(blank=True, null=True)
    idacademicyeardata = models.IntegerField(blank=True, null=True)
    duplicatesametrack = models.IntegerField(blank=True, null=True)
    duplicatedifftrack = models.IntegerField(blank=True, null=True)
    isloapublish = models.IntegerField(blank=True, null=True)
    idpublishloasessiondata = models.IntegerField(blank=True, null=True)
    isloapublish_onlinetest = models.IntegerField(blank=True, null=True)
    isloaextensionpublish = models.IntegerField(blank=True, null=True)
    is_autoloaextensionpublish = models.IntegerField(blank=True, null=True)
    idpublishloaextensionsessiondata = models.IntegerField(blank=True, null=True)
    is_autoloapublish = models.IntegerField(blank=True, null=True)
    is_autoloapublish_viawa = models.IntegerField(blank=True, null=True)
    dateloapublish = models.DateTimeField(blank=True, null=True)
    isloarepublish = models.IntegerField(blank=True, null=True)
    islatpublish = models.IntegerField(blank=True, null=True)
    is_autolatpublish_viawa = models.IntegerField(blank=True, null=True)
    islat2publish = models.IntegerField(blank=True, null=True)
    islat3publish = models.IntegerField(blank=True, null=True)
    islat4publish = models.IntegerField(blank=True, null=True)
    islcdnpublish = models.IntegerField(blank=True, null=True)
    iddatamedfinalrank = models.IntegerField(blank=True, null=True)
    ispaid = models.IntegerField(blank=True, null=True)
    paymentamount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_forceautoloa_2020 = models.IntegerField(blank=True, null=True)
    iswithdrawn = models.IntegerField(blank=True, null=True)
    withdrawnby = models.IntegerField(blank=True, null=True)
    isenrolled = models.IntegerField(blank=True, null=True)
    israporsubmit = models.IntegerField(blank=True, null=True)
    israporreceivedby = models.IntegerField(blank=True, null=True)
    isprestasisubmit = models.IntegerField(blank=True, null=True)
    isprestasireceivedby = models.IntegerField(blank=True, null=True)
    idtelemarketingdata = models.IntegerField(blank=True, null=True)
    idteleanswerdata = models.IntegerField(blank=True, null=True)
    is_oldmigrated = models.IntegerField(blank=True, null=True)
    is_rgmigrated = models.IntegerField(blank=True, null=True)
    is_rapormigrated = models.IntegerField(blank=True, null=True)
    is_profexemigrated = models.IntegerField(blank=True, null=True)
    is_earlyreg = models.IntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    iddatareligion = models.IntegerField(blank=True, null=True)
    pushprovince = models.IntegerField(blank=True, null=True)
    pushregencies = models.IntegerField(blank=True, null=True)
    ispushupdated = models.IntegerField(blank=True, null=True)
    ismypushupdated = models.IntegerField(blank=True, null=True)
    isassignnomovingin = models.IntegerField(blank=True, null=True)
    issentnomovingin = models.IntegerField(blank=True, null=True)
    isreserveroom = models.IntegerField(blank=True, null=True)
    isassignroomno = models.IntegerField(blank=True, null=True)
    idroomno = models.IntegerField(blank=True, null=True)
    roomno_queue = models.IntegerField(blank=True, null=True)
    needtemproom = models.IntegerField(blank=True, null=True)
    idroomtempno = models.IntegerField(blank=True, null=True)
    planstsnbh = models.TextField(blank=True, null=True)
    getstsnbh = models.TextField(blank=True, null=True)
    changetosingle = models.IntegerField(blank=True, null=True)
    roompriorityno = models.IntegerField(blank=True, null=True)
    assignroomby = models.IntegerField(blank=True, null=True)
    isassignschsib = models.IntegerField(blank=True, null=True)
    schsibby = models.IntegerField(blank=True, null=True)
    isassignschkjbbk = models.IntegerField(blank=True, null=True)
    schkjbbkby = models.IntegerField(blank=True, null=True)
    createvisaby = models.IntegerField(blank=True, null=True)
    is_reg_with_payment = models.IntegerField(blank=True, null=True)
    is_notifpaid_sent = models.IntegerField(blank=True, null=True)
    payment_status = models.TextField(blank=True, null=True)
    payment_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_servicefee = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_trxfee = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_withdrawn = models.IntegerField(blank=True, null=True)
    withdrawseq = models.IntegerField(blank=True, null=True)
    idgradform_rmsdata = models.IntegerField(blank=True, null=True)
    idgradform_tipekerjadata = models.IntegerField(blank=True, null=True)
    idgradform_ispresuniv = models.IntegerField(blank=True, null=True)
    idintlform_admissionterm = models.IntegerField(blank=True, null=True)
    iddatatipeangsuran = models.IntegerField(blank=True, null=True)
    idconcentrationgraduatedata = models.IntegerField(blank=True, null=True)
    is_inquiryresign = models.IntegerField(blank=True, null=True)
    refundpaid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_medicaldata_verified = models.IntegerField(blank=True, null=True)
    med_is_stage1_pass = models.IntegerField(blank=True, null=True)
    med_is_stage2_paid = models.IntegerField(blank=True, null=True)
    med_is_stage2_pass = models.IntegerField(blank=True, null=True)
    med_is_stage3_pass = models.IntegerField(blank=True, null=True)
    datestamp = models.DateTimeField(blank=True, null=True)
    idcreated = models.IntegerField(blank=True, null=True)
    idmodify = models.IntegerField(blank=True, null=True)
    cicilan_terms1amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms1due = models.DateTimeField(blank=True, null=True)
    cicilan_terms2amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms2due = models.DateTimeField(blank=True, null=True)
    cicilan_terms3amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms3due = models.DateTimeField(blank=True, null=True)
    cicilan_terms4amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms4due = models.DateTimeField(blank=True, null=True)
    cicilan_terms5amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms5due = models.DateTimeField(blank=True, null=True)
    cicilan_terms6amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms6due = models.DateTimeField(blank=True, null=True)
    cicilan_terms7amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms7due = models.DateTimeField(blank=True, null=True)
    cicilan_terms8amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms8due = models.DateTimeField(blank=True, null=True)
    idregbranddata = models.IntegerField(blank=True, null=True)
    umur = models.IntegerField(blank=True, null=True)
    age_imputed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cicilan_terms1due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms2due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms3due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms4due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms5due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms6due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms7due_known = models.IntegerField(blank=True, null=True)
    cicilan_terms8due_known = models.IntegerField(blank=True, null=True)
    dateloapublish_known = models.IntegerField(blank=True, null=True)
    total_cicilan = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    assumed_enrolled = models.BooleanField(blank=True, null=True)
    label_bayar = models.IntegerField(blank=True, null=True)
    label_enroll = models.IntegerField(blank=True, null=True)
    finalscore_bin_left = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    finalscore_bin_right = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eda_2023_2024'


class Genders(models.Model):
    id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'


class GroupRegistrasi(models.Model):
    iddatagroupreg = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'group_registrasi'


class Groups(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class JenisSekolah(models.Model):
    idschooltypedata = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jenis_sekolah'


class JurusanSekolah(models.Model):
    idschooljurusandata = models.IntegerField(primary_key=True)
    idschooltypedata = models.ForeignKey(JenisSekolah, models.DO_NOTHING, db_column='idschooltypedata')
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'jurusan_sekolah'


class Major(models.Model):
    idmajordata = models.IntegerField(primary_key=True)
    idfacultydata = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    displayname = models.CharField(max_length=150, blank=True, null=True)
    majorcode = models.CharField(max_length=10, blank=True, null=True)
    is_pagi = models.IntegerField(blank=True, null=True)
    is_malam = models.IntegerField(blank=True, null=True)
    iddataeducationlevel = models.IntegerField(blank=True, null=True)
    idspecialtermsrankdata = models.IntegerField(blank=True, null=True)
    linkvideo = models.TextField(blank=True, null=True)
    akreditasi = models.CharField(max_length=5, blank=True, null=True)
    is_displayreportrevenue = models.IntegerField(blank=True, null=True)
    ipcreated = models.CharField(max_length=50, blank=True, null=True)
    datecreated = models.CharField(max_length=50, blank=True, null=True)
    idcreated = models.IntegerField(blank=True, null=True)
    ipmodify = models.CharField(max_length=50, blank=True, null=True)
    datemodify = models.CharField(max_length=50, blank=True, null=True)
    idmodify = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major'


class Provinsi(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'provinsi'


class Questions(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class Regency(models.Model):
    id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Provinsi, models.DO_NOTHING)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regency'


class Registrants(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.TextField(blank=True, null=True)
    idnumber = models.TextField(blank=True, null=True)
    school = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    regtype = models.TextField(blank=True, null=True)
    regtime = models.TextField(blank=True, null=True)
    gender = models.ForeignKey(Genders, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrants'


class RegistrasiKhusus(models.Model):
    iddataregkhusustype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrasi_khusus'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Sessions(models.Model):
    id = models.BigAutoField(primary_key=True)
    session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class TipeKelas(models.Model):
    iddataclasstype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipe_kelas'


class TipeRegistrasi(models.Model):
    iddataregtype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    displayname = models.CharField(max_length=100, blank=True, null=True)
    reg_displayname = models.CharField(max_length=100, blank=True, null=True)
    groupreg_displayname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipe_registrasi'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'




        
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
    # Gunakan ForeignKey untuk menghubungkan ke Provinsi
    province = models.ForeignKey(Provinsi, models.DO_NOTHING, db_column='province_id')
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'regency'
        verbose_name_plural = 'Regencies'

    def __str__(self):
        return self.name

# Sekarang, definisikan model utama yang merujuk ke model di atas
# Kita akan memperbaiki Eda20232024 dan Eda20222023
class Eda20232024(models.Model):
    idregistrantdata = models.IntegerField(primary_key=True)
    
    # FIX: Ubah IntegerField menjadi ForeignKey
    # db_column memberitahu Django untuk menggunakan nama kolom yang ada di database
    iddataprovinces = models.ForeignKey(
        Provinsi, 
        models.DO_NOTHING, 
        db_column='iddataprovinces', 
        blank=True, 
        null=True
    )
    iddataregencies = models.ForeignKey(
        Regency, 
        models.DO_NOTHING, 
        db_column='iddataregencies', 
        blank=True, 
        null=True
    )
    
    # Kolom-kolom lain yang relevan (bisa disesuaikan)
    groupreg = models.CharField(max_length=255, blank=True, null=True)
    asalsekolah = models.CharField(max_length=255, blank=True, null=True)
    graduationyear = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    finalscore = models.FloatField(blank=True, null=True)
    isenrolled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eda_2023_2024'
        verbose_name = 'Data Pendaftar 2023/2024'
        verbose_name_plural = 'Data Pendaftar 2023/2024'

class Eda20222023(models.Model):
    idregistrantdata = models.IntegerField(primary_key=True)
    
    # FIX: Lakukan hal yang sama di sini
    iddataprovinces = models.ForeignKey(
        Provinsi, 
        models.DO_NOTHING, 
        db_column='iddataprovinces', 
        blank=True, 
        null=True
    )
    iddataregencies = models.ForeignKey(
        Regency, 
        models.DO_NOTHING, 
        db_column='iddataregencies', 
        blank=True, 
        null=True
    )
    
    # Kolom-kolom lain yang relevan (bisa disesuaikan)
    groupreg = models.CharField(max_length=255, blank=True, null=True)
    asalsekolah = models.CharField(max_length=255, blank=True, null=True)
    graduationyear = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    finalscore = models.FloatField(blank=True, null=True)
    isenrolled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eda_2022_2023'
        verbose_name = 'Data Pendaftar 2022/2023'
        verbose_name_plural = 'Data Pendaftar 2022/2023'

