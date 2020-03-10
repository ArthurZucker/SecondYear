from client import *
from openssl import *
import json
import base64
import time
c = Connection()
#Use kerberos to connect to uVm
#/bin/uVM/e1a7f6c2

#4919

def get_stp(K,adess,vm_name = ""):
        dict = {'method':'GET','url':adess}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        gateway = "/bin/gateway"
        if(vm_name != ""):
            gateway = "/bin/uVM/{}/gateway".format(vm_name)
        response = c.post_raw(gateway,base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))



def post_stp(K,adress,args,vm_name =""):
        dict = {'method':'POST','url':adress,'args':args}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        gateway = "/bin/gateway"
        if(vm_name != ""):
            gateway = "/bin/uVM/{}/gateway".format(vm_name)
        response = c.post_raw(gateway,base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))


def get_auten(username,key):
    d = {'username': username, 'timestamp': time.time()}
    e = json.dumps(d)
    f = encrypt(e, key)
    return f

def kerberos(username,password,vm_name):
    dict = c.get("/bin/kerberos/authentication-service/{}".format(username))
    clef = decrypt(dict['Client-TGS-session-key'],password)
    print(clef)
    authenticator = get_auten(username,clef)
    dict2 = c.post("/bin/kerberos/ticket-granting-service",TGT=dict["TGT"],vm_name=vm_name,authenticator=authenticator)
    print(dict2)
    CSsk = decrypt(dict2['Client-Server-session-key'],clef)
    #Client-Server-ticket
    print(c.post("/bin/uVM/{}/hello".format(vm_name),ticket = dict2["Client-Server-ticket"],authenticator = get_auten(username,CSsk)))
    fail = "/knowledge-center/failsafe/"
    index = [0,1,2,3,4,5]
    try:
        print(get_stp(CSsk,"/",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/READ.ME",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/LEGAL",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/monitor-settings",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/firmware",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/ex-programmer",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/courthouse-hack",vm_name))
        #/knowledge-center/ex-programmer/<i>    avec    i = 0,1,2,3
        print("___*100")
        print(get_stp(CSsk,"/failsafe",vm_name))
        for i in index:
            print(get_stp(CSsk,"/knowledge-center/failsafe/{}".format(i),vm_name))

        print("___*100")
        print(get_stp(CSsk,"/backup-tape",vm_name))
        print(get_stp(CSsk,"/knowledge-center/backup-tape/0",vm_name))
    except Exception as e:
        print(decrypt_b64(e.msg,CSsk))


"""
Tout ça pour dire que nous aimerions bien accéder à la bande numéro 4919. Comme
par hasard, tous ceux qui ont essayé d'y accéder ont reçu un message d'erreur --
et quelques mois plus tard, ils avaient disparu de la circulation.

En attendant, il y a peut-être quelque chose à faire. Le message d'erreur est
signé par un opérateur. Il s'agit de signatures DSA. Seulement, on sait de
source sûre que l'implémentation de la signature possède un grave bug. En effet,
l'aléa utilisé est TOUJOURS LE MÊME (il a apparemment été hardcodé par un
programmeur qui n'avait pas compris la spécification). Quelqu'un qui a le temps,
et les compétences, pourra peut-être en tirer parti.
"""


password = "means"
username = "shane90"
vm_name = "e1a7f6c2"
kerberos(username,password,vm_name)
failsafe_password = "I_hope_you_never_logon_to_this"
