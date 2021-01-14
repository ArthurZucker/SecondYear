from client import *
from openssl import *
from sha256 import *
from blocks import *
import json
import binascii
import base64
import time
c = Connection()
with open("jennifergriffin","r") as f:
    user = f.readline().strip('\n')
    key = f.read()
    #print(user)
#print(key)
i =(c.get("/bin/login/passwordless"))
"""try:
    print(c.post("/bin/login/passwordless",user=user,response = base64.b64encode(sign(i["challenge"],key)).decode()))
except  Exception as e:
    #print(e.msg)
    #print(c.get("/bin/courthouse/shane90"))
    print(c.get("/bin/courthouse/database"))"""
asser = c.get("/bin/courthouse/database")
print(asser)
commande = base64.b64encode("; DELETE * FROM charges WHERE user='wilkinsonethan'".encode())
query = base64.b64encode(asser['query'].encode())
my_query ='; DELETE FROM charges WHERE user="wilkinsonethan"'
my_query ='; DELETE FROM charges WHERE username="shane90"'
#_--____________________________________________________________________________________
bin = "/bin/sha256sum"
k2  = "9y$B&E)H@MbQeThW"
tot = k2+asser['query']
print(c.post(bin,M=base64.b64encode(tot.encode()).decode()))
print(len(tot.encode())*8)
print(512-(len(tot.encode())*8)%512)
if(512-(len(tot.encode())*8)%512 < 64):
    raise Exception("cas non géré")

padlen = 512-(len(tot.encode())*8)%512-64
padlen = int(padlen/8)-2
print("padd len = ",padlen)
tot_len = (len(tot.encode())*8 + padlen)/8
print("longueure totale",tot_len)
print(hex(len(tot)*8))
i = int(hex(len(tot)*8), base=16)
h = "{0:016x}".format(i)
print("{0:016x}".format(i))
print(base64.b16decode(h))
padding = b'\x80\x00' + padlen*b'\x00' + base64.b16decode(h)
print(padding)
##Ok on a le bon badding, maintenant il nous faut le suffixe





s1 = sha256(tot.encode()+padding)
h1 =  s1.hexdigest()
print(h1)



tot2  = (k2+asser['query']).encode()+ padding + my_query.encode()

i = int(hex(len(tot2)*8), base=16)
h = "{0:016x}".format(i)
print(h)
padlen = 512-(len(tot2)*8)%512-64
padlen = int(padlen/8)-2
paddingleft = b'\x80\x00' + padlen*b'\x00' + base64.b16decode(h)
print(c.post(bin,M=base64.b64encode(tot2+paddingleft).decode()))
print(paddingleft)
final =  my_query.encode() + paddingleft
print(final)
final_send =  (asser['query']).encode()+ padding + my_query.encode()


s2 = sha256(final,IV=h1) #,IV=asser['mac']


print(s1.hexdigest())
print(s2.hexdigest())

s3 = sha256(final,IV=asser['mac']) #,IV=asser['mac']
h = s3.hexdigest()
post = "/bin/courthouse/database"
try:
    print(c.post(post,query = base64.b64encode(final_send).decode(),mac = h))
except Exception as e :
    print(e)

print(c.get("/home/shane90/INBOX"))