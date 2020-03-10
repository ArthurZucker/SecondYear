from client import *
from openssl import *
import json
import base64
c = Connection()

#print(c.post("/bin/login",user="guest",password="guest"))
#print(c.get("/home/"))

#mess = c.get("/home/guest/NASA.bin")
#cyphe = decrypt(mess, 'ISEC')
#print(cyphe)
#print(c.get("/home/guest/NASA.bin"))
print(c.post("/bin/login",user="wilkinsonethan",password="!r3YPa7u#&"))
IV = c.get("/sbin/monitor-settings")
log  = c.get("/bin/login/CHAP")
plaintext = "wilkinsonethan" + "-" + log['challenge']
response = encrypt(plaintext,"!r3YPa7u#&")
c.post("/bin/jukebox/disable")
c.post("/bin/jukebox/stop")
"""
def get_card(n):
        return c.get("/bin/banks/card-data/{}".format(n))

print(c.post("/bin/login/CHAP",user = "wilkinsonethan",response = response))
print(c.get("/bin/hackademy"))
print(c.get("/bin/hackademy/ticket/1813"))
a = (c.get("/bin/hackademy/ticket/1813/attachment/a"))
b = (c.get("/bin/hackademy/ticket/1813/attachment/b"))
n = (c.get("/bin/hackademy/ticket/1813/attachment/n"))
print(c.get("/bin/police_hq/ticket/684"))
client = (c.get("/bin/police_hq/ticket/684/attachment/client"))
sample = c.get("/bin/banks/forensics/sample")
print(c.get("/bin/banks/forensics"))
forensics = c.get("/bin/banks/forensics")
certificat = c.get("/bin/banks/CA")
print(sample)
print(sample['valid'])
print(verify(certificat,sample['transaction']))
dict = {}
dict['identifier'] = forensics['identifier']
dict['statuses'] = []
for card in forensics['card-numbers']:
        dict['statuses'].append(verify(certificat,get_card(card)))
print(dict)
print(c.post("/bin/sendmail",to=client['email'],subject="Vérification des transaction",content=dict))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/police_hq/ticket/684/close"))"""
# 'reason': 'Le carte contient une clef secrète qui ne correspond pas à son certificat (symptome probable : signature du challenge invalide).'}
#'La signature du challenge par la carte est invalide.'
#'Le nom de la banque et/ou le numéro de la carte dans le certificat de la carte ne correspondent pas aux données de la transaction.'
adress = "/service/hardware/status"
#i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
#print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))

K = "debug-me"
text = "Väinö".encode('utf-8')
text = base64.b64encode(text).decode()
dict = {'method':'PUT','url':'/bin/echo','data':text}
jdict =json.dumps(dict)
enc_jdict = encrypt(jdict,K)
response = c.post_raw("/bin/test-gateway",base64.b64decode(enc_jdict))
print(decrypt_b64(response,K))


nonce = c.post("/bin/login/stp",username="wilkinsonethan")
K = "!r3YPa7u#&"+'-'+nonce

def start_stp(K):
    test1 = "/bin/login/stp/handshake"
    dict = {'method':'GET','url':test1}
    jdict =json.dumps(dict)
    enc_jdict = encrypt(jdict,K)
    response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))

start_stp(K)
print(decrypt_b64(response,K))

text = "Väinö".encode('utf-8')
text = base64.b64encode(text).decode()
dict = {'method':'PUT','url':'/bin/echo','data':text}
jdict =json.dumps(dict)
enc_jdict = encrypt(jdict,K)
response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
print(decrypt_b64(response,K))

def get_mail_stp(key):
        test1 = "/home/wilkinsonethan/INBOX/unread"
        dict = {'method':'GET','url':test1}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        i = decrypt_b64(response,K)
        i = int((i.strip('[]').split(',')[0]))
        test1 = "/home/wilkinsonethan/INBOX/{}".format(i)
        dict = {'method':'GET','url':test1}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        try:
                response= c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
                return(decrypt_b64(response,K))
        except Exception as e:
                print(decrypt_b64(e.msg,K))

        return(decrypt_b64(response,K))

def get_stp(K,adess):
        dict = {'method':'GET','url':adess}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))

def post_stp(K,adress,args):
        dict = {'method':'POST','url':adress,'args':args}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))

dict = {'method':'GET','url':adress}
jdict =json.dumps(dict)
enc_jdict = encrypt(jdict,K)
response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
action = "/service/hardware/action/DOOR"

print(decrypt_b64(response,K))
print(get_stp(K,"/service/hardware/action"))
print(get_stp(K,"/service/hardware/action/DOOR"))
print(post_stp(K,action,{'action':'unlock'}))
try:
        print(post_stp(K,"/bin/police_hq/ticket/685/close",{}))
        print(get_stp(K,"/bin/police_hq/"))
except Exception as e:
        decrypt_b64(e.msg,K)

print(get_stp(K,"/bin/police_hq/ticket/1832"))
print(get_stp(K,"/bin/police_hq/ticket/1832/attachment/log"))
print(get_stp(K,"/bin/police_hq/ticket/1832/attachment/indication-0"))
print(get_stp(K,"/bin/police_hq/ticket/1832/attachment/indication-1"))
print(get_stp(K,"/bin/police_hq/ticket/1832/attachment/indication-2"))
print(get_stp(K,"/bin/police_hq/ticket/1832/attachment/indication-3"))
print(get_stp(K,"/bin/police_hq/ticket/1832/attachment/indication-4"))

#print(get_mail_stp(K))
