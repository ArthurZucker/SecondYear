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
c.post("/bin/jukebox/disable")
c.post("/bin/jukebox/stop")
"""
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
#c.post("/bin/hackademy/exam/arith/eq-lin-mod-p",X=X)
a = int(c.get("/bin/hackademy/ticket/1815/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1815/attachment/b"))
indic = c.get("/bin/hackademy/ticket/1815/attachment/indication-0")
print(indic)
"""
from random import randrange, getrandbits
def is_prime(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n-1:
            j = 1
            while j < s and x != n-1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
        return True


def generate_prime_candidate2(a,b):
    i = a
    while not is_prime(i):
        i+=1
    return i


def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length=64):
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 256):
        p = generate_prime_candidate(length)
    return p


"""
print(generate_prime_candidate2(a,b))
print(c.post("/bin/hackademy/exam/prime/range",p = generate_prime_candidate(a,b)))
print(c.post("/bin/hackademy/ticket/1815/close"))
"""


print(c.get("/bin/hackademy/ticket/1816"))
a = int(c.get("/bin/hackademy/ticket/1816/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1816/attachment/b"))
indic0 = c.get("/bin/hackademy/ticket/1816/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1816/attachment/indication-1")
print(indic0,indic1)
print(generate_prime_number())
list_prime = []
qp = b//(pow(2,64))
lima = a/qp
limb = b/qp
i = 10
qcourant = 3
list_prime.append(3)
while(qcourant < qp and i<60 and qcourant < b):
    v = generate_prime_number(i)
    if(v not in list_prime):
        list_prime.append(v)
        qcourant*=v
    else:
        i=i+2

x=1
for i in list_prime:
    x = x*i


print(a,"<\n",x,"<\n",b)
print(x<b)
print(list_prime)
print(c.post("/bin/hackademy/exam/prime/product",p=list_prime))
