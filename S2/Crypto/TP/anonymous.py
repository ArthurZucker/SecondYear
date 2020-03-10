from client import *
from openssl import *
import json
import base64
import time
c = Connection()
print(c.post("/bin/login",user="wilkinsonethan",password="!r3YPa7u#&"))
IV = c.get("/sbin/monitor-settings")
log  = c.get("/bin/login/CHAP")
plaintext = "wilkinsonethan" + "-" + log['challenge']
response = encrypt(plaintext,"!r3YPa7u#&")
c.post("/bin/jukebox/disable")
c.post("/bin/jukebox/stop")

#print(c.post("/bin/login",user="guest",password="guest"))
#print(c.get("/home/"))

#mess = c.get("/home/guest/NASA.bin")
#cyphe = decrypt(mess, 'ISEC')
#print(cyphe)
#print(c.get("/home/guest/NASA.bin"))
print(c.get("/bin/key-management/wilkinsonethan/signatures"))
k,s = genpkey()
print(c.post("/bin/key-management/upload-pk",public_key = k,confirm=True))
#Astrid
user1 = "apierce"
password1 = "THQ9TYIgr("

#Clement
user2 = "anthonyunderwood"
password2 = "&0GINr%A8@"

#Jerome
user3 = "mollythomas"
password3 = "(QWDtj0&_7"

user = [user1, user2, user3]
password = [password1,password2,password3]

def signer(username,password):
    pk = c.get("/bin/key-management/wilkinsonethan/pk")
    k,s = genpkey()
    print(k,s)
    print(c.post("/bin/login",user=username,password=password))
    print(c.post("/bin/key-management/upload-pk",public_key = k,confirm=True))
    print(c.post("/bin/login",user="wilkinsonethan",password="!r3YPa7u#&"))
    signature = sign(pk,s)
    dic = {}
    dic['signature'] = base64.b64encode(signature)
    dic['signer'] = username
    print(dic)
    print(c.post("/bin/key-management/upload-signature",signature = base64.b64encode(signature).decode(),signer = username))

"""
for (a,b) in zip(user,password):
    signer(a,b)

print(c.post("/bin/sendmail",to="anonymous.coward",subject="Faire attention",content="je te contacte afin d'avoir plus d'information"))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
serialized_dict = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/body")
dict = json.loads(serialized_dict)
session_key = pkencrypt(base64.b64decode((dict['session_key'].encode('utf-8'))),s,0)
print(session_key)
print(decrypt(dict['payload'],session_key.decode()))
"""
#Use kerberos to connect to uVm
#/bin/uVM/e1a7f6c2
#4919
dict = (c.get("/bin/long-term-storage/4919"))
while(dict['status']!="READY"):
    print(c.get("/bin/long-term-storage/4919"))
    dict = (c.get("/bin/long-term-storage/4919"))
