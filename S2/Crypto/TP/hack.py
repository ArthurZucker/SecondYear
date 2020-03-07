from client import *
from openssl import *
import json
import base64
import math
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
print(c.post("/bin/login/CHAP",user = "wilkinsonethan",response = response))
print(c.get("/bin/hackademy"))
print(c.get("/bin/hackademy/ticket/1813"))
a = int((c.get("/bin/hackademy/ticket/1813/attachment/a")))
b = int((c.get("/bin/hackademy/ticket/1813/attachment/b")))
n = int(c.get("/bin/hackademy/ticket/1813/attachment/n"))
temp=-1
for i in range(-n,0):
    if(math.log((a*i +b)%n,2)<0):
        print(i)
    #print( math.log((a*i +b)%n,2))
print(temp)
c.post("/bin/hackademy/exam/arith/eq-lin-mod-p",X=X)
