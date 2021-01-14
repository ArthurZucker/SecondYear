
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

print(c.get("/bin/hackademy"))
print(c.get("/bin/hackademy/ticket/1820"))
print(c.get("/bin/hackademy/ticket/1820/attachment/indication-0"))
print(c.get("/bin/hackademy/ticket/1820/attachment/indication-1"))
print(c.get("/bin/hackademy/ticket/1820/attachment/indication-2"))

def create_hachage_table(g,p,T):
    H={}
    print(T)
    print(h)
    print("Calcul de la table de Hachage ...")
    for i in range(0,T):
        print((T,i))
        H[pow(g,i,p)]=i
    return H

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

def calcul_log(g,p,h,T,H):#faire varier T si jamais ça c'est long
    print("Calcul de x ...")
    S=modinv(pow(g,T,p),p)
    u=h
    i=0
    while(u not in H):
        print(i)
        u=(u*S)%p
        i=i+1
    return i*T+H[u]

i=8#i de 1 à 8 plus c'est haut plus plus c'est long t'as de points
res=c.get("/bin/hackademy/exam/discrete-log/challenge/"+str(i))
p=int(res["p"])
h=int(res["h"])
g=int(res["g"])#premier

T=getrandbits(18)#essaye 20 19 17 si jamais ça marche pas
H=create_hachage_table(g,p,T)
x=calcul_log(g,p,h,T,H)
print(c.post("/bin/hackademy/exam/discrete-log/challenge/"+str(i),x=x))
