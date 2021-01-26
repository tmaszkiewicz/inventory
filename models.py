from django.db import models
from django import forms
from django.contrib.admin import widgets
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class windowsLicense(models.Model):
    key = models.CharField(max_length=255, blank=True)
    available = models.IntegerField(default=0)
    inUse = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    osName = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)


class windowsSvrLicense(models.Model):
    key = models.CharField(max_length=255, blank=True)
    available = models.IntegerField(default=0)
    inUse = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    osName = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    def delete(self):
        return self.delete()

    def __str__(self):
        return self.osName + self.description + self.key
class officeLicense(models.Model):
    key = models.CharField(max_length=255, blank=True)
    available = models.IntegerField(default=0, blank =True)
    inUse = models.IntegerField(default=0, blank=True)
    free = models.IntegerField(default=0, blank=True)
    description = models.CharField(max_length=255, blank=True)
    vol = models.CharField(max_length=255, blank=True)
    #ver = models.CharField(max_length=255, blank=True)
    #date = models.CharField(max_length=255, blank=True)
    def delete(self):
        return self.delete()

    def __str__(self):
        return self.description + self.key
class user(models.Model):
    cn = models.CharField(max_length=50, blank=True)
    distinguishedName = models.CharField(max_length=255, blank=True)
    memberOf = models.CharField(max_length=255, blank=True)
    primaryGroupID = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    sAMAccountName = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.cn +";"+ self.distinguishedName +";"+self.memberOf+";"+self.primaryGroupID+";"+self.name+";"+self.sAMAccountName

class machine(models.Model):
    cn = models.CharField(max_length=50, blank=True)
    operatingSystem = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    operatingSystemServicePack = models.CharField(max_length=255, blank=True)
    distinguishedName = models.CharField(max_length=255, blank=True)
    OU = models.CharField(max_length=255, blank=True)
    aktualizacja = models.DateTimeField(auto_now=True, blank = True)
    dNSHostName = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(user,on_delete=models.SET_NULL,null=True, blank=True)
    windowsLicense = models.ForeignKey(windowsLicense,on_delete=models.SET_NULL, null=True, blank=True)
    officeLicense = models.ForeignKey(officeLicense,on_delete=models.SET_NULL, null=True, blank=True)
    rodo = models.BooleanField(default=True)
    #rodo = models.CharField(max_length=255, blank=True,default="True")
    def __str__(self):
        return self.cn +" "+ self.operatingSystem

class svr(models.Model):
    cn = models.CharField(max_length=50, blank=True)
    operatingSystem = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    operatingSystemServicePack = models.CharField(max_length=255, blank=True)
    distinguishedName = models.CharField(max_length=255, blank=True)
    OU = models.CharField(max_length=255, blank=True)
    dNSHostName = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(user,on_delete=models.SET_NULL,null=True, blank=True)
    windowsSvrLicense = models.ForeignKey(windowsSvrLicense,on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
        return self.cn +" "+ self.operatingSystem

class term(models.Model):

    sn = models.CharField(max_length=30, blank=True)
    hostname = models.CharField(max_length=30, blank=True,null=True)
    model =  models.CharField(max_length=30, blank=True,null=True)
    mac = models.CharField(max_length=30, blank=True,null=True)
    description = models.CharField(max_length=255, blank=True,null=True)
    dep = models.CharField(max_length=30, blank=True,null=True)
    def __str__(self):
        return str(self.hostname) + " " + str(self.sn)
class foamFile(models.Model):
    fileName = models.CharField(max_length=30,blank=True,null=True)
    def __str__(self):
        return str(self.fileName)
class foamRow(models.Model):
    foamFile = models.ForeignKey(foamFile,on_delete=models.SET_NULL,blank=True,null=True)
    plant = models.CharField(max_length=10,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    workCenter=models.CharField(max_length=10,blank=True,null=True)
    tura = models.CharField(max_length=10,blank=True,null=True)
    ta = models.CharField(max_length=10,blank=True,null=True)
    kol6 = models.CharField(max_length=10,blank=True,null=True)
    kol7 = models.CharField(max_length=10,blank=True,null=True)
    OrderNo = models.CharField(max_length=20,blank=True,null=True) #Etykieta
    kol9 = models.CharField(max_length=20,blank=True,null=True)
    IndexSap = models.CharField(max_length=20,blank=True,null=True) # Prawdopodobnie index SAP
    IndexSapNazwa = models.CharField(max_length=40,blank=True,null=True) # Prawdopodobnie nazwa indeksu SAP
    kol12 = models.CharField(max_length=20,blank=True,null=True)
    kol13 = models.CharField(max_length=20,blank=True,null=True)
    kol14 = models.CharField(max_length=20,blank=True,null=True)
    kol15 = models.CharField(max_length=20,blank=True,null=True)
    kol16 = models.CharField(max_length=20,blank=True,null=True)
    kol17 = models.CharField(max_length=20,blank=True,null=True)
    kol18 = models.CharField(max_length=20,blank=True,null=True)
    kol19 = models.CharField(max_length=20,blank=True,null=True)
    fulfilled = models.NullBooleanField(blank=True,null=True,default=False)
    def __str__(self):
        return str(self.foamFile)+" "+ str(self.workCenter) +" "+ str(self.tura)
class message(models.Model):
    MessageId = models.CharField(max_length=60, blank=True,null=True)
    MessageType = models.CharField(max_length=30,blank=True,null=True)
    TimeStamp = models.CharField(max_length=40,blank=True,null=True)
    TimeClient = models.DateTimeField(blank=True,null=True)
    TimeManual = models.DateTimeField(blank=True,null=True)

    MachineId = models.CharField(max_length=30,blank=True,null=True)
    TerminalId = models.CharField(max_length=30,blank=True,null=True)
    WorkCenterId = models.CharField(max_length=30,blank=True,null=True)
    EmployeeId = models.CharField(max_length=30,blank=True,null=True)
    TimeCardNr = models.CharField(max_length=30,blank=True,null=True)
    OrderNr = models.CharField(max_length=30,blank=True,null=True)
    OperationNr = models.IntegerField(blank=True,null=True)
    ConfirmationNr = models.IntegerField(blank=True,null=True)
    Plant = models.CharField(max_length=30,blank=True,null=True)
    Shift = models.IntegerField(blank=True,null=True)
    WageGroup =models.CharField(max_length=30,blank=True,null=True)
    IsProcessed = models.NullBooleanField(blank=True,null=True)
    def  __str__(self):
        return str(self.OrderNr)# + self.TerminalId #+ self.TimeClient
        
class termShift(models.Model):
    TYP = (
    (1, 'Przyjęcie'),
    (2, 'Wydanie'),
    (3, 'Wyslany do naprawy'),
    (4, 'Przyjecie z naprawy'),
    (5, 'Utylizacja'),
    )
    eventDate = models.DateTimeField(blank=True,null=True,default=now())
    hostnameBefore = models.CharField(max_length=30, blank=True,null=True)
    hostnameAfter = models.CharField(max_length=30, blank=True,null=True)
    depBefore = models.CharField(max_length=30, blank=True,null=True)
    depAfter = models.CharField(max_length=30, blank=True,null=True)
    odbierajacy = models.CharField(max_length=30, blank=True,null=True)
    wydajacy = models.CharField(max_length=30, blank=True,null=True)
    description = models.TextField(default=None)
    typ = models.IntegerField(choices=TYP, default=None)
    term = models.ForeignKey(term,on_delete=models.SET_NULL,null=True, blank=True)
    def __str__(self):
        return  self.hostnameBefore + self.hostnameAfter + "     " + str(self.typ) + "     " + str(self.term.sn)
class lastRefresh(models.Model):
    lastRefresh = models.DateTimeField(blank=True,null=True,default=now())
    def __str__(self):    
        return str(self.lastRefresh)
#FORMS
class term_form(forms.ModelForm):
    class Meta:
        model = term
        fields = ('sn','hostname','model','mac','description','dep')
    
class machine_form(forms.ModelForm):
    class Meta:
        model = machine
        fields = ('cn','operatingSystem','description','operatingSystemServicePack','distinguishedName','dNSHostName', 'user','windowsLicense', 'officeLicense','rodo')

class svr_form(forms.ModelForm):
    class Meta:
        model = svr
        fields = ('cn','operatingSystem','description','operatingSystemServicePack','distinguishedName','dNSHostName', 'user', 'windowsSvrLicense')
class windowsSvrLicense_form(forms.ModelForm):
    class Meta:
        model = windowsSvrLicense
        fields = ('key','available','inUse','free','osName','description')
class windowsLicense_form(forms.ModelForm):
    class Meta:
        model = windowsSvrLicense
        fields = ('key','available','inUse','free','osName','description')
class officeLicense_form(forms.ModelForm):
    class Meta:
        model = officeLicense
        fields = ('key','available','inUse','free','description','vol')
class termShift_form(forms.ModelForm):
    class Meta:
        model = termShift
        labels = {
        }
        fields = {'hostnameBefore','hostnameAfter', 'depBefore', 'depAfter', 'odbierajacy', 'wydajacy', 'description', 'typ','eventDate'}
        #widgets = {'date': forms.DateInput(attrs={'class':'datepicker'}),}
