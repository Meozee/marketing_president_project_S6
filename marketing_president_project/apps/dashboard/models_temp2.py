# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Reg20222024(models.Model):
    idregistrantdata = models.BigIntegerField(blank=True, null=True)
    groupreg = models.BigIntegerField(blank=True, null=True)
    regtype = models.BigIntegerField(blank=True, null=True)
    iddataregkhusustype = models.BigIntegerField(blank=True, null=True)
    isregtypechanged = models.BigIntegerField(blank=True, null=True)
    oldregtype = models.BigIntegerField(blank=True, null=True)
    regtypechangeby = models.BigIntegerField(blank=True, null=True)
    regtypechangedate = models.FloatField(blank=True, null=True)
    regtypechangehour = models.FloatField(blank=True, null=True)
    is_onlinetest = models.BigIntegerField(blank=True, null=True)
    is_onlinetest_taken = models.BigIntegerField(blank=True, null=True)
    qty_onlinetest_taken = models.BigIntegerField(blank=True, null=True)
    is_tryout = models.BigIntegerField(blank=True, null=True)
    namalengkap = models.TextField(blank=True, null=True)
    idnumber = models.TextField(blank=True, null=True)
    asalsekolah = models.TextField(blank=True, null=True)
    idschooltypedata = models.BigIntegerField(blank=True, null=True)
    idschooljurusandata = models.BigIntegerField(blank=True, null=True)
    graduationyear = models.FloatField(blank=True, null=True)
    highschoolcountry = models.BigIntegerField(blank=True, null=True)
    highschoolattendyear = models.TextField(blank=True, null=True)
    dob = models.TextField(blank=True, null=True)
    age_on_register = models.BigIntegerField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    idmajordata = models.BigIntegerField(blank=True, null=True)
    idconcentrationdata = models.BigIntegerField(blank=True, null=True)
    idmajordata2_dualdegree = models.BigIntegerField(blank=True, null=True)
    iddataclasstype = models.BigIntegerField(blank=True, null=True)
    ismajorchanged = models.BigIntegerField(blank=True, null=True)
    oldmajor = models.BigIntegerField(blank=True, null=True)
    majorchangeby = models.BigIntegerField(blank=True, null=True)
    majorchangedate = models.TextField(blank=True, null=True)
    majorchangehour = models.TextField(blank=True, null=True)
    noreg = models.BigIntegerField(blank=True, null=True)
    ideventdata = models.BigIntegerField(blank=True, null=True)
    parentname = models.TextField(blank=True, null=True)
    parentjob = models.TextField(blank=True, null=True)
    parentinstitution = models.TextField(blank=True, null=True)
    parentyearlyincome = models.TextField(blank=True, null=True)
    maritalstatus = models.TextField(blank=True, null=True)
    nationality = models.BigIntegerField(blank=True, null=True)
    idcountrydata = models.BigIntegerField(blank=True, null=True)
    iddataprovinces = models.BigIntegerField(blank=True, null=True)
    iddataregencies = models.BigIntegerField(blank=True, null=True)
    kelurahan = models.TextField(blank=True, null=True)
    kecamatan = models.TextField(blank=True, null=True)
    alamatrumah = models.TextField(blank=True, null=True)
    intl_streetname = models.TextField(blank=True, null=True)
    intl_state = models.TextField(blank=True, null=True)
    intl_city = models.TextField(blank=True, null=True)
    intl_country = models.BigIntegerField(blank=True, null=True)
    isaddresscheck = models.BigIntegerField(blank=True, null=True)
    isaddresscheckedby = models.BigIntegerField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    passportno = models.TextField(blank=True, null=True)
    passportexpiredate = models.TextField(blank=True, null=True)
    essay1personality = models.FloatField(blank=True, null=True)
    essay2choosepresuniv = models.FloatField(blank=True, null=True)
    essay3choosemajor = models.FloatField(blank=True, null=True)
    iddatawhyuniv = models.BigIntegerField(blank=True, null=True)
    reasonwhyuniv = models.TextField(blank=True, null=True)
    iddatawhymajor = models.BigIntegerField(blank=True, null=True)
    reasonwhymajor = models.TextField(blank=True, null=True)
    iddatainfouniv = models.BigIntegerField(blank=True, null=True)
    reasoninfouniv = models.TextField(blank=True, null=True)
    puatscore = models.BigIntegerField(blank=True, null=True)
    puetscore = models.BigIntegerField(blank=True, null=True)
    finalscore = models.BigIntegerField(blank=True, null=True)
    rank = models.TextField(blank=True, null=True)
    isrankchanged = models.BigIntegerField(blank=True, null=True)
    oldrank = models.BigIntegerField(blank=True, null=True)
    rankchangeby = models.BigIntegerField(blank=True, null=True)
    rankchangedate = models.TextField(blank=True, null=True)
    rankchangehour = models.TextField(blank=True, null=True)
    is_raporautorank = models.BigIntegerField(blank=True, null=True)
    is_prestasiautorank = models.BigIntegerField(blank=True, null=True)
    is_utbkautorank = models.BigIntegerField(blank=True, null=True)
    is_unbkautorank = models.BigIntegerField(blank=True, null=True)
    iddatatipelulusanprofexe = models.BigIntegerField(blank=True, null=True)
    profexe_asaluniv = models.TextField(blank=True, null=True)
    profexe_asalprodi = models.TextField(blank=True, null=True)
    profexe_asalipk = models.TextField(blank=True, null=True)
    iddatapassingstatus = models.BigIntegerField(blank=True, null=True)
    exampassdate = models.FloatField(blank=True, null=True)
    exampasslocation = models.FloatField(blank=True, null=True)
    examscore = models.FloatField(blank=True, null=True)
    isrankconfirm = models.BigIntegerField(blank=True, null=True)
    isrankedby = models.BigIntegerField(blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    referral = models.TextField(blank=True, null=True)
    referralwithdrawid = models.TextField(blank=True, null=True)
    referralwithdrawseq = models.BigIntegerField(blank=True, null=True)
    iddatawithdrawstatus = models.BigIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    idacademicyeardata = models.BigIntegerField(blank=True, null=True)
    duplicatesametrack = models.BigIntegerField(blank=True, null=True)
    duplicatedifftrack = models.BigIntegerField(blank=True, null=True)
    isloapublish = models.BigIntegerField(blank=True, null=True)
    idpublishloasessiondata = models.BigIntegerField(blank=True, null=True)
    isloapublish_onlinetest = models.BigIntegerField(blank=True, null=True)
    isloaextensionpublish = models.BigIntegerField(blank=True, null=True)
    is_autoloaextensionpublish = models.BigIntegerField(blank=True, null=True)
    idpublishloaextensionsessiondata = models.BigIntegerField(blank=True, null=True)
    is_autoloapublish = models.BigIntegerField(blank=True, null=True)
    is_autoloapublish_viawa = models.BigIntegerField(blank=True, null=True)
    dateloapublish = models.TextField(blank=True, null=True)
    hourloapublish = models.TextField(blank=True, null=True)
    isloarepublish = models.BigIntegerField(blank=True, null=True)
    dateloarepublish = models.TextField(blank=True, null=True)
    hourloarepublish = models.TextField(blank=True, null=True)
    dateloaextensionpublish = models.TextField(blank=True, null=True)
    hourloaextensionpublish = models.TextField(blank=True, null=True)
    islatpublish = models.BigIntegerField(blank=True, null=True)
    is_autolatpublish_viawa = models.BigIntegerField(blank=True, null=True)
    datelatpublish = models.TextField(blank=True, null=True)
    hourlatpublish = models.TextField(blank=True, null=True)
    islat2publish = models.BigIntegerField(blank=True, null=True)
    datelat2publish = models.TextField(blank=True, null=True)
    hourlat2publish = models.TextField(blank=True, null=True)
    islat3publish = models.BigIntegerField(blank=True, null=True)
    datelat3publish = models.FloatField(blank=True, null=True)
    islat4publish = models.BigIntegerField(blank=True, null=True)
    datelat4publish = models.FloatField(blank=True, null=True)
    isluapublish = models.FloatField(blank=True, null=True)
    dateluapublish = models.FloatField(blank=True, null=True)
    islcdnpublish = models.BigIntegerField(blank=True, null=True)
    datelcdnpublish = models.FloatField(blank=True, null=True)
    iddatamedfinalrank = models.BigIntegerField(blank=True, null=True)
    ispaid = models.BigIntegerField(blank=True, null=True)
    paymentamount = models.BigIntegerField(blank=True, null=True)
    paymentdate = models.TextField(blank=True, null=True)
    is_forceautoloa_2020 = models.BigIntegerField(blank=True, null=True)
    iswithdrawn = models.BigIntegerField(blank=True, null=True)
    withdrawnby = models.BigIntegerField(blank=True, null=True)
    withdrawndate = models.FloatField(blank=True, null=True)
    withdrawnhour = models.FloatField(blank=True, null=True)
    isenrolled = models.BigIntegerField(blank=True, null=True)
    israporsubmit = models.BigIntegerField(blank=True, null=True)
    raporsubmitdate = models.TextField(blank=True, null=True)
    israporreceivedby = models.BigIntegerField(blank=True, null=True)
    isprestasisubmit = models.BigIntegerField(blank=True, null=True)
    prestasisubmitdate = models.FloatField(blank=True, null=True)
    isprestasireceivedby = models.BigIntegerField(blank=True, null=True)
    examloc = models.FloatField(blank=True, null=True)
    birthplace = models.TextField(blank=True, null=True)
    approachby = models.FloatField(blank=True, null=True)
    idtelemarketingdata = models.BigIntegerField(blank=True, null=True)
    idteleanswerdata = models.BigIntegerField(blank=True, null=True)
    telelastdate = models.TextField(blank=True, null=True)
    is_oldmigrated = models.BigIntegerField(blank=True, null=True)
    is_rgmigrated = models.BigIntegerField(blank=True, null=True)
    is_rapormigrated = models.BigIntegerField(blank=True, null=True)
    rgmigratethirdparty = models.TextField(blank=True, null=True)
    migratecollectionperiod = models.TextField(blank=True, null=True)
    is_profexemigrated = models.BigIntegerField(blank=True, null=True)
    is_earlyreg = models.BigIntegerField(blank=True, null=True)
    kelas = models.TextField(blank=True, null=True)
    pengalaman = models.TextField(blank=True, null=True)
    raporlink = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    iddatareligion = models.BigIntegerField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    instagram = models.TextField(blank=True, null=True)
    pushprestasi = models.TextField(blank=True, null=True)
    pushcar = models.TextField(blank=True, null=True)
    pushnamaayah = models.TextField(blank=True, null=True)
    pushnamaibu = models.TextField(blank=True, null=True)
    pushalamatortu = models.FloatField(blank=True, null=True)
    pushprovince = models.BigIntegerField(blank=True, null=True)
    pushregencies = models.BigIntegerField(blank=True, null=True)
    pushkelurahan = models.FloatField(blank=True, null=True)
    pushkecamatan = models.FloatField(blank=True, null=True)
    pushtelp = models.TextField(blank=True, null=True)
    pushtelp2 = models.TextField(blank=True, null=True)
    pushhpayah = models.TextField(blank=True, null=True)
    pushhpibu = models.TextField(blank=True, null=True)
    pushemailortu = models.TextField(blank=True, null=True)
    pushrelationship = models.TextField(blank=True, null=True)
    pushrelationshipother = models.FloatField(blank=True, null=True)
    emergencyname = models.TextField(blank=True, null=True)
    emergencyalamat = models.TextField(blank=True, null=True)
    emergencytelprumah = models.TextField(blank=True, null=True)
    emergencynohp = models.TextField(blank=True, null=True)
    emergencyemail = models.TextField(blank=True, null=True)
    emergencyrelationship = models.TextField(blank=True, null=True)
    tipekamar = models.TextField(blank=True, null=True)
    aturkamar = models.TextField(blank=True, null=True)
    roomatenoreg = models.TextField(blank=True, null=True)
    roomatenoregstatus = models.FloatField(blank=True, null=True)
    roomatenoregnotes = models.FloatField(blank=True, null=True)
    bayarkamar = models.TextField(blank=True, null=True)
    pushstudentsick = models.TextField(blank=True, null=True)
    pushbloodtype = models.TextField(blank=True, null=True)
    pushsickrequest = models.TextField(blank=True, null=True)
    pushnaphabit = models.TextField(blank=True, null=True)
    pushlearnhabit = models.TextField(blank=True, null=True)
    pushstudentsport = models.TextField(blank=True, null=True)
    pushstudenthobby = models.TextField(blank=True, null=True)
    ispushupdated = models.BigIntegerField(blank=True, null=True)
    ismypushupdated = models.BigIntegerField(blank=True, null=True)
    movinginnumber = models.FloatField(blank=True, null=True)
    movingindate = models.FloatField(blank=True, null=True)
    movinginmintime = models.FloatField(blank=True, null=True)
    movingintime = models.FloatField(blank=True, null=True)
    movinginmaxtime = models.FloatField(blank=True, null=True)
    isassignnomovingin = models.BigIntegerField(blank=True, null=True)
    issentnomovingin = models.BigIntegerField(blank=True, null=True)
    isreserveroom = models.BigIntegerField(blank=True, null=True)
    isassignroomno = models.BigIntegerField(blank=True, null=True)
    idroomno = models.BigIntegerField(blank=True, null=True)
    roomno_status = models.FloatField(blank=True, null=True)
    roomno_queue = models.BigIntegerField(blank=True, null=True)
    dateroombookingexpired = models.FloatField(blank=True, null=True)
    sharingbedno = models.FloatField(blank=True, null=True)
    needtemproom = models.BigIntegerField(blank=True, null=True)
    idroomtempno = models.BigIntegerField(blank=True, null=True)
    planstsnbh = models.BigIntegerField(blank=True, null=True)
    getstsnbh = models.BigIntegerField(blank=True, null=True)
    changetosingle = models.BigIntegerField(blank=True, null=True)
    roompriorityno = models.BigIntegerField(blank=True, null=True)
    assignroomid = models.FloatField(blank=True, null=True)
    assignroomdate = models.FloatField(blank=True, null=True)
    assignroomhour = models.FloatField(blank=True, null=True)
    assignroomby = models.BigIntegerField(blank=True, null=True)
    isassignschsib = models.BigIntegerField(blank=True, null=True)
    schsibby = models.BigIntegerField(blank=True, null=True)
    schsibdate = models.FloatField(blank=True, null=True)
    schsibhour = models.FloatField(blank=True, null=True)
    isassignschkjbbk = models.BigIntegerField(blank=True, null=True)
    schkjbbkby = models.BigIntegerField(blank=True, null=True)
    schkjbbkdate = models.FloatField(blank=True, null=True)
    schkjbbkhour = models.FloatField(blank=True, null=True)
    createvisaby = models.BigIntegerField(blank=True, null=True)
    createvisadate = models.FloatField(blank=True, null=True)
    createvisahour = models.FloatField(blank=True, null=True)
    roomno = models.FloatField(blank=True, null=True)
    is_reg_with_payment = models.BigIntegerField(blank=True, null=True)
    is_notifpaid_sent = models.BigIntegerField(blank=True, null=True)
    payment_id = models.TextField(blank=True, null=True)
    payment_token = models.TextField(blank=True, null=True)
    payment_status = models.BigIntegerField(blank=True, null=True)
    payment_subtotal = models.FloatField(blank=True, null=True)
    payment_servicefee = models.FloatField(blank=True, null=True)
    payment_trxfee = models.FloatField(blank=True, null=True)
    payment_total = models.FloatField(blank=True, null=True)
    is_withdrawn = models.BigIntegerField(blank=True, null=True)
    withdrawalpaymentid = models.FloatField(blank=True, null=True)
    withdrawseq = models.BigIntegerField(blank=True, null=True)
    idgradform_rmsdata = models.BigIntegerField(blank=True, null=True)
    idgradform_tipekerjadata = models.BigIntegerField(blank=True, null=True)
    idgradform_ispresuniv = models.BigIntegerField(blank=True, null=True)
    idintlform_admissionterm = models.BigIntegerField(blank=True, null=True)
    iddatatipeangsuran = models.BigIntegerField(blank=True, null=True)
    idconcentrationgraduatedata = models.BigIntegerField(blank=True, null=True)
    is_inquiryresign = models.BigIntegerField(blank=True, null=True)
    refundpaid = models.BigIntegerField(blank=True, null=True)
    is_medicaldata_verified = models.BigIntegerField(blank=True, null=True)
    med_is_stage1_pass = models.BigIntegerField(blank=True, null=True)
    med_is_stage2_paid = models.BigIntegerField(blank=True, null=True)
    med_is_stage2_pass = models.BigIntegerField(blank=True, null=True)
    med_is_stage3_pass = models.BigIntegerField(blank=True, null=True)
    ipcreated = models.TextField(blank=True, null=True)
    datestamp = models.TextField(blank=True, null=True)
    hourstamp = models.TextField(blank=True, null=True)
    idcreated = models.BigIntegerField(blank=True, null=True)
    ipmodify = models.TextField(blank=True, null=True)
    datemodify = models.TextField(blank=True, null=True)
    idmodify = models.BigIntegerField(blank=True, null=True)
    cicilan_terms1amount = models.FloatField(blank=True, null=True)
    cicilan_terms1due = models.TextField(blank=True, null=True)
    cicilan_terms2amount = models.FloatField(blank=True, null=True)
    cicilan_terms2due = models.TextField(blank=True, null=True)
    cicilan_terms3amount = models.FloatField(blank=True, null=True)
    cicilan_terms3due = models.TextField(blank=True, null=True)
    cicilan_terms4amount = models.FloatField(blank=True, null=True)
    cicilan_terms4due = models.TextField(blank=True, null=True)
    cicilan_terms5amount = models.FloatField(blank=True, null=True)
    cicilan_terms5due = models.TextField(blank=True, null=True)
    cicilan_terms6amount = models.FloatField(blank=True, null=True)
    cicilan_terms6due = models.TextField(blank=True, null=True)
    cicilan_terms7amount = models.FloatField(blank=True, null=True)
    cicilan_terms7due = models.TextField(blank=True, null=True)
    cicilan_terms8amount = models.FloatField(blank=True, null=True)
    cicilan_terms8due = models.TextField(blank=True, null=True)
    idregbranddata = models.BigIntegerField(blank=True, null=True)
    asalsekolah_backup = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REG2022_2024'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DatasetUploadHistory(models.Model):
    id_data = models.AutoField(primary_key=True)
    nama_data = models.CharField(max_length=255)
    file_path = models.CharField(max_length=100)
    tanggal_upload = models.DateTimeField()
    tanggal_approve = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10)
    approver = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    uploader = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='datasetuploadhistory_uploader_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataset_upload_history'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GroupRegistrasi(models.Model):
    iddatagroupreg = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'group_registrasi'


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


class Reg20222024(models.Model):

    class Meta:
        managed = False
        db_table = 'reg2022_2024'


class Regency(models.Model):
    id = models.IntegerField(primary_key=True)
    province = models.ForeignKey(Provinsi, models.DO_NOTHING)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regency'


class RegistrasiKhusus(models.Model):
    iddataregkhusustype = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrasi_khusus'


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


class UploadData(models.Model):
    id_data = models.AutoField(primary_key=True)
    nama_data = models.TextField(blank=True, null=True)
    tanggal_upload = models.DateField(blank=True, null=True)
    tanggal_approve = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_data'
