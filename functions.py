import re
import ldap
import csv
import time,datetime
from .models import user,foamFile,foamRow,message,svr,machine,lastRefresh
#from datetime import datetime
from os import listdir
from os.path import isfile, join
def check_credentials(username, password,filtr,type):
    """Verifies credentials for username and password.
    Returns None on success or a string describing the error on failure
    # Adapt to your needs
    """
    LDAP_SERVER = 'ldap://192.168.41.40'
    # fully qualified AD user name
    LDAP_USERNAME = '%s@jan.polipol.intra' % username
    print(LDAP_USERNAME)
    # your password
    LDAP_PASSWORD = password
    #print(LDAP_PASSWORD)
    attrs = ['memberOf']
    try:
        # build a client
        ldap_client = ldap.initialize(LDAP_SERVER)
        # perform a synchronous bind
        ldap_client.set_option(ldap.OPT_REFERRALS,0)
        ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
    except ldap.INVALID_CREDENTIALS:
        ldap_client.unbind()
        return 'Wrong username /  password'
    except ldap.SERVER_DOWN:
        return 'AD server not available'
   # all is well
   # get all user groups and store it in cerrypy session for future use
    if type=='pc':
        workstations = read_machines(ldap_client,"DC=jan,DC=polipol,DC=intra",filtr)
    else:
        servers = read_svr(ldap_client,"DC=jan,DC=polipol,DC=intra",filtr)
    ldap_client.unbind()
    return None
def check_credentials_users(username, password):
    """Verifies credentials for username and password.
    Returns None on success or a string describing the error on failure
    # Adapt to your needs
    """
    LDAP_SERVER = 'ldap://192.168.41.40'
    # fully qualified AD user name
    LDAP_USERNAME = '%s@jan.polipol.intra' % username
    #print(LDAP_USERNAME)
    # your password
    LDAP_PASSWORD = password
    #print(LDAP_PASSWORD)
    attrs = ['memberOf']
    try:
        # build a client
        ldap_client = ldap.initialize(LDAP_SERVER)
        # perform a synchronous bind
        ldap_client.set_option(ldap.OPT_REFERRALS,0)
        ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
    except ldap.INVALID_CREDENTIALS:
        ldap_client.unbind()
        return 'Wrong username /  password'
    except ldap.SERVER_DOWN:
        return 'AD server not available'
   # all is well
   # get all user groups and store it in cerrypy session for future use
    read_users(ldap_client,"DC=jan,DC=polipol,DC=intra")
    ldap_client.unbind()
    return None
def read_machines(ldap_client,base_dn,filtr):
    #filtr1="(&(cn=jan-svr-*)(|(ou:dn:=SERVER)(ou:dn:=Computers))(!(cn=*-pr-*)))"
    results = ldap_client.search_s(base_dn,ldap.SCOPE_SUBTREE,filtr)
    for dn,entry in results:
        try:    
            cn = entry['cn'][0]
        
            try:
                operatingSystem = entry['operatingSystem'][0]
            except:
                operatingSystem = ""
            try:
                description = entry['description'][0]
            except:
                description = ""
            try:
                dNSHostName = entry['dNSHostName'][0]
            except:
                dNSHostName = ""
            try:
                distinguishedName = entry['distinguishedName'][0]
            except:
                distinguishedName = ""
            try:
                tmp1 = entry['distinguishedName'][0]
                tmp2 = tmp1[0:len(tmp1)]
                tmp3 = tmp2.decode().split(",")[1].split("=")[1]
                OU = tmp3
            except:
                OU = ""
            try:
                operatingSystemServicePack = entry['operatingSystemServicePack'][0]
            except:
                operatingSystemServicePack = ""
            if(machine.objects.filter(cn=cn).first() == None):
                comp = machine()
            else:
                comp = machine.objects.filter(cn=cn).first()
            comp.cn = cn
            comp.operatingSystem = operatingSystem
            comp.description= description
            comp.dNSHostName = dNSHostName
            comp.distinguishedName = distinguishedName
            comp.OU = OU
            comp.operatingSystemServicePack = operatingSystemServicePack
            #comp.aktualizacja = datetime.now()
            comp.save()
                
        except:
            None
    return None
def read_svr(ldap_client,base_dn,filtr):
    #results = ldap_client.search_s(base_dn,ldap.SCOPE_SUBTREE,"(&(cn=jan-svr*)(!(cn=*-pr-*)))" )
    #filtr1="(&(cn=jan-svr-*)(|(ou:dn:=SERVER)(ou:dn:=Computers))(!(cn=*-pr-*)))"
    filtr1="(&(cn=jan-svr-*)(!(cn=*-pr-*)))"

    results = ldap_client.search_s(base_dn,ldap.SCOPE_SUBTREE,filtr1)
    for dn,entry in results:
        try:
            cn = entry['cn'][0]
            try:
                operatingSystem = entry['operatingSystem'][0]
            except:
                operatingSystem = ""
            try:
                description = entry['description'][0]
            except:
                description = ""
            try:
                dNSHostName = entry['dNSHostName'][0]
            except:
                dNSHostName = ""
            try:
                distinguishedName = entry['distinguishedName'][0]
            except:
                distinguishedName = ""
            try:
                tmp1 = entry['distinguishedName'][0]
                tmp2 = tmp1[0:len(tmp1)]
                tmp3 = tmp2.decode().split(",")[1].split("=")[1]
                OU = tmp3
                
            except:
                OU = ""
            try:
                operatingSystemServicePack = entry['operatingSystemServicePack'][0]
            except:
                operatingSystemServicePack = ""
            
            if(svr.objects.filter(cn=cn).first() == None):
                comp = svr()
            else:
                comp = svr.objects.filter(cn=cn).first 
            comp.cn = cn
            comp.operatingSystem = operatingSystem
            comp.description= description
            comp.dNSHostName = dNSHostName
            comp.distinguishedName = distinguishedName
            comp.OU = OU
            comp.operatingSystemServicePack = operatingSystemServicePack
            comp.save()
        except:
            None
            #print(entry)
    return None
def read_users(ldap_client,base_dn):
    results = ldap_client.search_s(base_dn,ldap.SCOPE_SUBTREE,"(sAMAccountType=805306368)")
    for dn,entry in results:
        try:
            cn = entry['cn'][0]
            try:
                distinguishedName = entry['distinguishedName'][0]
            except:
                distinguishedName = ""
            #try:
            #    memberOf = entry['memberOf'][0]
            #except:
            #    memberOf= ""
            #    print("2")
            try:
                primaryGroupID = entry['primaryGroupID'][0]
            except:
                primaryGroupID= ""
            try:
                name = entry['name'][0]
                
            except:
                name = ""
            try:
                sAMAccountName= entry['sAMAccountName'][0]
            except:
                SamAccountName = ""
            usr = user()
            usr.cn = cn
            usr.name = name
            usr.primaryGroupID = primaryGroupID 
            usr.distinguishedName = distinguishedName
            usr.sAMAccountName = sAMAccountName
            #usr.memberOf = memberOfmemberOf
            
            usrcmp = user.objects.filter(name=name.decode())
            #if len(usrcmp)<3:
            #    print(usrcmp)
            #if usrcmp[0].name[:1] == 'M':
            #    print(usrcmp[0].name)
        
            #print(user.objects.filter(name=usr.name)[0])
            if len(usrcmp)==0:
                usr.save()
            else:
                None
        except:
            None
       
    return None
def msqlquery(svr, user, psw, db, qry):
    import pymssql
    conn = pymssql.connect(svr,user, psw, db, qry)
    cursor = conn.cursor(as_dict=True)
    cursor.execute(qry)
    #for each in cursor:
    #    print(each['TimeClient'])
        
    return cursor
def delete_unrelated():
    users = user.objects.all()  
    k=0
    #.prefetch_related('machine_set')[0]
    for u in users:
        #m = u.prefetch_related('machine_set')[0]
        try:
            print(u.machine_set.first().cn)
        except:
            print(u, "-to be deleted")
            k+=1
            u.delete()
        print(k)
    #    for i in u.machine_set.all():
    #        print(i.cn)
    #for u in users:
    #    print(u.name,u.machine_set)
    #for u in users:
    #    print (u.machine_set.first())
def readFoam():
    mypath="/media/jan-svr-misc01/Foam/archive"
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    for i in files:
        if foamFile.objects.all().filter(fileName=i):
            None
        else:
            foamF = foamFile()
            foamF.fileName=i
            foamF.save()
            with open("/".join([mypath,i]),'rt') as archive:
                rows = csv.reader(archive,delimiter=';',quotechar='|')
                print ("*************")
                #print(rows)
                for row in rows:
                    foamR=foamRow()
                    foamR.foamFile = foamF
                    #print(row)                    
                    foamR.plant = row[0]
                    foamR.date = row[1][:4]+"-"+row[1][4:6]+"-"+row[1][6:8]
                    #row 3 - > empty
                    foamR.workCenter=row[3]
                    foamR.tura=row[4]
                    #row6 - empty
                    foamR.ta=row[6]
                    foamR.kol6=row[7]
                    foamR.kol7=row[8]
                    foamR.OrderNo=row[9]
                    foamR.kol9=row[10]
                    foamR.IndexSap=row[11]
                    foamR.IndexSapNazwa=row[12]
                    foamR.kol12=row[13]
                    foamR.kol13=row[14]
                    foamR.kol14=row[15]
                    foamR.kol15=row[16]
                    foamR.kol16=row[17]
                    foamR.kol17=row[18]
                    foamR.kol18=row[19]
                    foamR.save()
    return True
def readMessages():
    timestamp = time.time()   
    effDate = datetime.datetime.now()+datetime.timedelta(days=-1)
    #print(str(effDate))
    #sql = "SELECT * FROM MESSAGE WHERE TimeClient >" +"'"+str(effDate)+"' and TimeClient> '"+str(lastRefresh.objects.last().lastRefresh)+"'"  #'2018-10-16 14:13:34'"
    #print(sql)
    #cursor = msqlquery('jan-svr-spot01\SQLEXPRESS', 'spot_sql', 'IDsQE8T5', 'SFC-Polipol',sql)

#------
    #row = cursor.fetchone()

    #while row:
    #    print(row)
#----

#    for each in cursor:        
#        msg = message()
#        msgId=message.objects.filter(MessageId=each['MessageId']).first()
        #print(msgId)
#        if msgId==None:
#            msg.MessageId = each['MessageId']
#            msg.MessageType = each['MessageType']
            ##msg.TimeStamp = each['TimeStamp']
#            msg.TimeClient = each['TimeClient']
#            msg.TimeManual = each['TimeManual']
#            msg.MachineId = each['MachineId']
#            msg.TerminalId  = each['TerminalId']
#            msg.WorkCenterId  = each['WorkCenterId']
#            msg.EmployeeId = each['EmployeeId']
#            msg.TimeCardNr = each['TimeCardNr']
#            msg.OrderNr  = each['OrderNr']
#            msg.OperationNr = each['OperationNr']
#            msg.ConfirmationNr = each['ConfirmationNr']
#            msg.Plant = each['Plant']
#            msg.Shift= each['Shift']
#            msg.WageGroup = each['WageGroup']
#            msg.IsProcessed = each['IsProcessed']
#            try:
#                msg.save()
#            except:
#                print("Błąd - message nie dodana")

    
    lastRefr = lastRefresh()
    lastRefr.lastRefresh =  datetime.datetime.now()
    lastRefr.save()
    #print(effDate)
    return True

def FulfillFoam():
    OrderLst = []
    for i in message.objects.all():
        OrderLst.append(i.OrderNr)

 
    notFulfiledFoams=foamRow.objects.exclude(OrderNo__in=OrderLst)

    
    for notFulfilledF in notFulfiledFoams:
        print(notFulfilledF.OrderNo)
        
    #    mesg = message.objects.filter(OrderNr=notFulfilledF.OrderNo).first()
    #    if mesg != None:
    #        print(notFulfilledF,"aaaaaa",mesg.OrderNo,"--- ",notFulfilledF.OrderNo)
    #        print(mesg)
    #        notFulfilledF.fullFilled = True
    #        notFulfilledF.save()
    #print(notFulfiledFoams)
    return True
    
