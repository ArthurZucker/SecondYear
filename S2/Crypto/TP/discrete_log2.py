
from client import *
from openssl import *
import random
import numpy as np
import json
import base64
import math
c = Connection()

#Astrid
user1 = "apierce"
password1 = "THQ9TYIgr("

user1 = "wilkinsonethan"
password1 = "!r3YPa7u#&"
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c
print(c.post("/bin/login",user=user1,password=password1))
IV = c.get("/sbin/monitor-settings")
log  = c.get("/bin/login/CHAP")
plaintext = user1 + "-" + log['challenge']
response = encrypt(plaintext,password1)
print(c.post("/bin/login/CHAP",user = user1,response = response))
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


def generate_prime_number(length=2048):
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 256):
        p = generate_prime_candidate(length)
    return p


def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0



def modinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b



"""
e=c.get("/bin/hackademy/ticket/1824/attachment/e")
e=int(e)

p=generate_prime_number()
q=generate_prime_number()
phi_n=(p - 1)*(q - 1)
a,b,c1=xgcd(e,phi_n)
while(phi_n<e and a!=1):
    print("la")
    p=generate_prime_number()
    q=generate_prime_number()
n=p*q
d=modinv(e,phi_n)
print(d<phi_n)

rep=c.post("/bin/hackademy/exam/rsa/keygen",n=n)
chiffre=rep['ciphertext']
m=pow(chiffre,d,n)
i = int("0x"+str(m), base=16)
kk = m.to_bytes(len(str(m)), byteorder='big')
print(kk)
c.post("/bin/hackademy/ticket/1824/close")
"""



"""
p=int(c.get("/bin/hackademy/ticket/1821/attachment/p"))
g=int(c.get("/bin/hackademy/ticket/1821/attachment/g"))

chiffre=c.get("/bin/hackademy/exam/elgamal/malleability")
a=chiffre['ciphertext'][0]
b=chiffre['ciphertext'][1]
pk=chiffre['PK']#g puissance x mod p avec x secret de bob

rep=c.post("/bin/hackademy/exam/elgamal/malleability",a=a,b=2*b%p)#dechiffrer le chiffre (a,2*b)
m=rep['m']#2m
m=m*modinv(2,p)%p#on divise par deux du coup
i = int("0x"+str(m), base=16)
kk = m.to_bytes(len(str(m)), byteorder='big')
print(kk)


p=int(c.get("/bin/hackademy/ticket/1822/attachment/p"))
g=int(c.get("/bin/hackademy/ticket/1822/attachment/g"))
print(g)
x=30000000000000000000000000000000000000000000000000000
print(x)
h=power(g,x,p)
res=c.post("/bin/hackademy/exam/elgamal/decryption",h=h)
#
c1=res['ciphertext'][0]
c2=res['ciphertext'][1]
m=c2*modinv(power(c1,x,p),p)%p
i = int("0x"+str(m), base=16)
kk = m.to_bytes(len(str(m)), byteorder='big')
print(kk)

"""
print(c.get("/bin/hackademy/ticket/1826/attachment/indication-0"))
print(c.get("/bin/hackademy/ticket/1826/attachment/indication-1"))
print(c.get("/bin/hackademy/ticket/1826/attachment/indication-2"))

e=int(c.get("/bin/hackademy/ticket/1826/attachment/e"))
n=int(c.get("/bin/hackademy/ticket/1826/attachment/n"))
rep=c.get("/bin/hackademy/exam/rsa/most-significant-bit")
# print(e)
# print(n)
C=int(rep['ciphertext'])
# print(C)
def trouver_clair(C,e,n):
    a=0
    b=n
    i=0
    C_prime=C
    bool=True

    while(bool):
        if(a==b):
            if(pow(a,e,n)==C):
                 return a
            else:
                i = int("0x"+str(a), base=16)
                kk = a.to_bytes(len(str(a)), byteorder='big')
                print(kk)
                a=a+1
                print("CORRECTION")
        else:
            C_prime=(pow(pow(2,i),e)*C)%n
            rep=c.post("/bin/hackademy/exam/rsa/most-significant-bit",c=C_prime)
            print(rep)
            if(rep['MSB']==True):
                a=(a+b)//2
            else:
                b=(a+b)//2
            print((a,b))
            i=i+1

m=trouver_clair(C,e,n)
i = int("0x"+str(m), base=16)
kk = m.to_bytes(len(str(m)), byteorder='big')
print(kk)

c.post("/bin/hackademy/ticket/1817/close")
c.post("/bin/hackademy/ticket/1821/close")
