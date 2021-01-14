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
        #aller a /courthouse-hack
        print("___*100")
        print(get_stp(CSsk,"/monitor-settings",vm_name))
        #/sbin/monitor-settings
        # utiliser block.py
        #Une requête GET sur ce programme renvoie un message chiffré.
        #Une requête POST doit être accompagnée de deux arguments "ciphertext" et "IV". encodé en base64
        #i = 0,1,2,3
        print("___*100")
        print(get_stp(CSsk,"/firmware",vm_name))
        print("___*100")
        print(get_stp(CSsk,"/ex-programmer",vm_name))
        ex = json.loads(get_stp(CSsk,"/ex-programmer/infos",vm_name))
        print(get_stp(CSsk,"/ex-programmer/infos",vm_name))
        with open(ex['username'],"w") as f:
            f.write(ex['username'])
            f.write(ex['sk'])
        index2 = [0,1,2,3]
        for i in index2:
            print(get_stp(CSsk,"/knowledge-center/ex-programmer/{}".format(i),vm_name))
        print("___*100")
        print(get_stp(CSsk,"/courthouse-hack",vm_name))
        print(get_stp(CSsk,"/knowledge-center/courthouse-hack/0",vm_name))
        print(get_stp(CSsk,"/knowledge-center/courthouse-hack/1",vm_name))
        print(get_stp(CSsk,"/knowledge-center/courthouse-hack/2",vm_name))
        print(get_stp(CSsk,"/knowledge-center/courthouse-hack/3",vm_name))
        print(get_stp(CSsk,"/knowledge-center/courthouse-hack/4",vm_name))
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

En effet, une signature DSA est une
paire (r, s) où r et s sont deux entiers modulo q

Tout d'abord, le webservice renvoie la signature encodée en base64. Mais une
fois qu'on a défait l'encodage base64, le décodage n'est pas fini !

Les signatures produites par openssl sont sérialisées en ASN.1. On trouve sur
internet des utilitaires permettant de déconstruire ce genre de données. Mais en
fait openssl lui-même en contient un : c'est la commande "openssl asn1parse".
(ne pas hésiter à consulter "man asn1parse").

*) le premier octet est la valeur 0x30 (qui indique qu'on a affaire à une
   séquence de plusieurs valeurs).

*) le deuxième octet indique la taille des valeurs sérialisées ensuite.
   En principe, cette taille est de 68 octets.

*) le troisième octet doit êre 0x02 (qui indique que ce qui suit est un entier).

*) le quatrième octet doit être la taille de cet entier (c'est r). En principe,
   cet entier occupe 32 octets (256 bits, normal, il est donc modulo q).

*) les octets [4:36] sont la représentation big-endian du premier entier de la
   signature.

*) l'octet qui suit (d'offset 36, en principe) doit être 0x02, qui indique que
   ce qui suit est un entier (c'est s).

*) l'octet qui suit (d'offset 37, en principe) doit être la taille de cet
   entier. En principe, cet entier occupe 32 octets (256 bits, normal, il est
   donc modulo q).

*) les octets [38:70] sont la représentation big-endian du deuxième entier de la
   signature.


"""


password = "means"
username = "shane90"
vm_name = "e1a7f6c2"
kerberos(username,password,vm_name)
failsafe_password = "I_hope_you_never_logon_to_this"
