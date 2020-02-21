from client import *
from openssl import *
import base64
c = Connection()
#print(c.post("/bin/login",user="guest",password="guest"))
#print(c.get("/home/"))

#mess = c.get("/home/guest/NASA.bin")
#cyphe = decrypt(mess, 'ISEC')
#print(cyphe)
#print(c.get("/home/guest/NASA.bin"))
print(c.post("/bin/login",user="wilkinsonethan",password="!r3YPa7u#&"))
#print(c.get("/sbin/monitor-settings"))
IV = c.get("/sbin/monitor-settings")
#print(c.get("/home/wilkinsonethan"))
#print(c.get("/home/wilkinsonethan/bye-bye.txt"))
#print(c.get("/home/wilkinsonethan/INBOX"))
#print(c.get("/home/wilkinsonethan/INBOX/4250"))
#print(c.get("/bin/crypto_helpdesk"))
#print(c.get("/bin/crypto_helpdesk/ticket/493"))
## TUtoriel
#attachement = c.get("/bin/crypto_helpdesk/ticket/493/attachment/fetch-me")
#mail = (c.get("/bin/crypto_helpdesk/ticket/493/attachment/client"))['email']
#dic = {'foo':attachement,'bar':42}
#print(dic)
#print("______\n",mail,"\n____\n")
#print(c.post("/bin/sendmail",to=mail,subject="Tutoriel",content=dic))
#print(c.post("/bin/crypto_helpdesk/ticket/493/close"))

##Ticket 2
#attachement = c.get("/bin/crypto_helpdesk/ticket/494/attachment/password")
#mail = "omarschwartz"
#data = c.get("/bin/long-term-storage/1024")
#message = c.get("/bin/long-term-storage/device/17b9264b")
#cypher = encrypt(message,attachement)
#print(c.post("/bin/sendmail",to=mail,subject="Beltran Group",content=cypher))

## Tciket 3
#cipher = c.get("/bin/crypto_helpdesk/ticket/495/attachment/cipher")
#mdp = c.get("/bin/crypto_helpdesk/ticket/495/attachment/password")
#mail = "hawkinsjesse"
#cipher_text = c.get("/bin/crypto_helpdesk/ticket/495/attachment/ciphertext")
#print(cipher)
#real_message = decrypt(cipher_text,mdp,cipher = cipher)
#print(decrypt(cipher_text,mdp,cipher = cipher))
#print(c.post("/bin/sendmail",to=mail,subject="Problème de déchiffrement (méthode inhabituelle)",content=real_message))
log  = c.get("/bin/login/CHAP")
plaintext = "wilkinsonethan" + "-" + log['challenge']
response = encrypt(plaintext,"!r3YPa7u#&")

print(c.post("/bin/login/CHAP",user = "wilkinsonethan",response = response))

""" message = c.get("/bin/crypto_helpdesk/ticket/517/attachment/message")
public_key = c.get("/bin/crypto_helpdesk/ticket/517/attachment/public-key")
mail = c.get("/bin/crypto_helpdesk/ticket/517/attachment/client")['email']
cypher = pkencrypt(message,public_key)
print(cypher)
cypher = base64.b64encode(cypher).decode()
print(c.post("/bin/sendmail",to=mail,subject="Message à chiffrer (clef publique)",content=cypher))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/crypto_helpdesk/ticket/517/close")) """

"""
print(c.get("/bin/crypto_helpdesk/ticket/518"))
id  = c.get("/bin/crypto_helpdesk/ticket/518/attachment/contact")
client = c.get("/bin/crypto_helpdesk/ticket/518/attachment/client")
message = "informations très très très sensibles"
key = c.get("/bin/key-management/"+id)
cypher = pkencrypt(message,key)
cypher = base64.b64encode(cypher).decode()
k,s = genpkey()
print(k,s)
print(c.post("/bin/key-management/upload-pk",public_key = k,confirm=True))
print(c.post("/bin/sendmail",to=id,subject="Message à chiffrer (clef publique)",content=cypher))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
send = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/body")
print(send)
print(len(send.encode('utf-8')))
mess = pkencrypt(base64.b64decode(send),s,0)
print(mess.decode())
print(c.post("/bin/sendmail",to=client['email'],subject="Message à chiffrer (clef publique)",content=mess.decode()))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/crypto_helpdesk/ticket/518/close"))

## Ticket 519
print(c.get("/bin/crypto_helpdesk/ticket/519"))
contact  = c.get("/bin/crypto_helpdesk/ticket/519/attachment/contact")
client = c.get("/bin/crypto_helpdesk/ticket/519/attachment/client")
client_pk = c.get(("/bin/key-management/{}/pk").format(contact))
temp_key = "Ab560plfjcuaoddI3"
print(temp_key)
reciprocity = c.get("/bin/crypto_helpdesk/ticket/519/attachment/reciprocity")
session_key = pkencrypt(temp_key,client_pk)
session_key = (base64.b64encode(session_key).decode())
# Encrypt the payload
payload = encrypt(reciprocity,temp_key)
content = {'session_key':session_key,'payload':payload}
print(c.post("/bin/sendmail",to=contact,subject="Message à chiffrer (clef hybrid)",content=content))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
print(c.post("/bin/crypto_helpdesk/ticket/519/close"))
## Contrat de travaik
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
email = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/sender")
contract = c.get("/home/wilkinsonethan/INBOX/"+str(i)+"/body")

print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
signed = sign(contract,s)
print(c.post("/bin/sendmail",to=email,subject="Votre nouveau contrat de travail",content=base64.b64encode(signed).decode()))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))
"""

def sxor(s1,s2):    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

## SAV BYE BYE
print(c.get("/bin/police_hq"))
print(c.get("/bin/police_hq/ticket/683"))
text_fileb64 = c.get("/bin/police_hq/ticket/683/attachment/exhibit-A")
print(text_fileb64)
text_file = base64.b64decode(text_fileb64)
plain_pbmb64 = c.get("/bin/police_hq/ticket/683/attachment/exhibit-B")
plain_pbm = base64.b64decode(plain_pbmb64)
i = c.get("/bin/police_hq/ticket/683/attachment/i")
j = c.get("/bin/police_hq/ticket/683/attachment/j")

key = sxor(text_fileb64, plain_pbmb64)
size = len(key)
mask0 = "0"*size
mask1 = "1"*size
print(text_file.decode())
print(sxor(key,mask0).encode('utf-8'))
print(sxor(key,mask1).encode('utf-8'))
print(sxor(sxor(key,mask0),mask1).encode('utf-8'))


"""
sample =  c.get("/bin/police_hq/ticket/683/attachment/sample")

with open('image.pbm', 'w') as fd:
	fd.write(sample)

print(c.get("/bin/police_hq/ticket/683/attachment/exhibit-A"))
print(c.get("/bin/police_hq/ticket/683/attachment/exhibit-B"))
print(c.get("/bin/police_hq/ticket/683/attachment/sample"))
print(c.get("/bin/police_hq/ticket/683/attachment/indication-0"))
print(c.get("/bin/police_hq/ticket/683/attachment/indication-1"))
print(c.get("/bin/police_hq/ticket/683/attachment/indication-2"))
"""




