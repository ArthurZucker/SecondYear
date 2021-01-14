from client import *
from openssl import *
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
#print(c.post("/bin/login",user="guest",password="guest"))
#print(c.get("/home/"))

#mess = c.get("/home/guest/NASA.bin")
#cyphe = decrypt(mess, 'ISEC')
#print(cyphe)
#print(c.get("/home/guest/NASA.bin"))
#print(c.post("/bin/login",user="wilkinsonethan",password="!r3YPa7u#&"))
print(c.post("/bin/login",user=user1,password=password1))
IV = c.get("/sbin/monitor-settings")
log  = c.get("/bin/login/CHAP")
plaintext = user1 + "-" + log['challenge']
response = encrypt(plaintext,password1)
print(c.post("/bin/login/CHAP",user = user1,response = response))
print(c.get("/bin/hackademy"))
c.post("/bin/jukebox/disable")
c.post("/bin/jukebox/stop")

print(c.post("/bin/hackademy/ticket/1819/close"))
print(c.post("/bin/hackademy/ticket/1820/close"))
print(c.post("/bin/hackademy/ticket/1826/close"))
print(c.get("/home/wilkinsonethan/INBOX"))
i = c.get("/home/wilkinsonethan/INBOX/unread")[0]
print(c.get("/home/wilkinsonethan/INBOX/"+str(i)))

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
    while (not is_prime(i) and i<b):
        i+=1
    if(not is_prime(i)):
        raise NameError('No prime found between a and b ')
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
print(generate_prime_candidate2(a,b))
print(c.post("/bin/hackademy/exam/prime/range",p = generate_prime_candidate(a,b)))
print(c.post("/bin/hackademy/ticket/1815/close"))
"""
"""
print(c.get("/bin/hackademy/ticket/1813"))

a = int(c.get("/bin/hackademy/ticket/1813/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1813/attachment/b"))
n = int(c.get("/bin/hackademy/ticket/1813/attachment/n"))

# a*X = -b %n
# X = -b*a^-1 %n

print(xgcd(a,n))
_,x,y = xgcd(a,n)

X = (x*(-b))%n
print((a*X + b) %n)
print(c.post("/bin/hackademy/exam/arith/eq-lin-mod-p",X=X))
c.get("/bin/hackademy/ticket/1813/close"))

"""


def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c
"""
print(c.get("/bin/hackademy/ticket/1822"))
p=int(c.get("/bin/hackademy/ticket/1822/attachment/p"))
g=int(c.get("/bin/hackademy/ticket/1822/attachment/g"))
print(g)
x=30000000000000000000000000000000000000000000000000000
print(x)
h=power(g,x,p)
res=c.post("/bin/hackademy/exam/elgamal/decryption",h=h)

c1=res['ciphertext'][0]
c2=res['ciphertext'][1]
m=c2*modinv(power(c1,x,p),p)%p
# print(m)
# h=hex(m)
# print(h)
size_m = int.bit_length(m)
i = int("0x"+str(m), base=16)
kk = m.to_bytes(len(str(m)), byteorder='big')
print(kk)
"""

def primes():
    yield 2 # 2 est le seul nombre premier PAIR
    D = {}  # D[n] = 2*p ---> p est le plus petit facteur premier de n
    q = 3   # nombre (impair) dont on teste la primalité
    while True:
        two_p = D.pop(q, None)  # connait-on un nombre premier qui divise q ?
        if two_p:               # OUI : q n'est pas premier, car p le divise.
            # assert q % (two_p // 2) == 0
            x = q + two_p           # Pour maintenir le dictionnaire D, on
            while x in D:           # cherche le prochain multiple (impair) de
                x += two_p          # p qui n'a pas de diviseurs inférieurs à
            D[x] = two_p            # p, et marquer qu'il est divisible par p.
                                    # astuce : q et p sont impair, donc q+p est
                                    #     pair. On passe donc directement à
                                    #     q + 2p.
        else:                   # NON : q est premier.
            D[q*q] = 2*q        # q*q est le plus petit nombre composite qui n'a
                                # pas de facteurs plus petits que q
            yield q             # Renvoie q
        q += 2

"""
print(c.get("/bin/hackademy/ticket/1816"))
a = int(c.get("/bin/hackademy/ticket/1816/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1816/attachment/b"))
indic0 = c.get("/bin/hackademy/ticket/1816/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1816/attachment/indication-1")
print(indic0,indic1)

qp = b//(pow(2,64))
taille = int.bit_length(qp)
list_prime = []
qcourant = 1

for p in primes():
    qcourant*=p
    list_prime.append(p)
    if(qcourant>qp):
        break
    if p > 1e6:
            break


qcourant = 1
ll = []
#On prend des grands nombres premiers, dés qu'on a un interval assez grand pour trouver un premier on va le chercher
for i in  range(int(len(list_prime))-1,0,-1):
    p = list_prime[i]
    qcourant*=p
    limi = (b-a)//qcourant
    ll.append(p)
    if(qcourant>qp and limi >  int.bit_length(b)):
        break
    if(limi == 0):
        raise Exception('limite dépassée')


lima = a//qcourant
limb = b//qcourant
last_prime = generate_prime_candidate2(lima+1,limb)
qcourant*=last_prime
ll.append(last_prime)
print(last_prime)
print(a<qcourant)
print(qcourant<b)
print(ll)
k = 1
for i in ll:
    k*=i
print(i)
print(i>a)
print(i<b)
print(qcourant == i)
print(c.post("/bin/hackademy/exam/prime/product",p=ll))

print(c.post("/bin/hackademy/ticket/1816/close"))
"""



"""Malleability EL Gamal """
# p=int(c.get("/bin/hackademy/ticket/1778/attachment/p"))
# g=int(c.get("/bin/hackademy/ticket/1778/attachment/g"))
#
# chiffre=c.get("/bin/hackademy/exam/elgamal/malleability")
# a=chiffre['ciphertext'][0]
# b=chiffre['ciphertext'][1]
# pk=chiffre['PK']#g puissance x mod p avec x secret de bob
#
# rep=c.post("/bin/hackademy/exam/elgamal/malleability",a=a,b=2*b%p)#dechiffrer le chiffre (a,2*b)
# m=rep['m']#2m
# m=m*modinv(2,p)%p#on divise par deux du coup
# i = int("0x"+str(m), base=16)
# kk = m.to_bytes(len(str(m)), byteorder='big')
# print(kk)

def generate_prime_number(length=2048):
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

""" RSA KEYGEN """
# e=c.get("/bin/hackademy/ticket/1781/attachment/e")
# e=int(e)
#
# p=generate_prime_number()
# q=generate_prime_number()
# phi_n=(p - 1)*(q - 1)
# while(phi_n<e):
#     print("la")
#     p=generate_prime_number()
#     q=generate_prime_number()
# n=p*q
# d=modinv(e,phi_n)
# print(d<phi_n)
#
# rep=c.post("/bin/hackademy/exam/rsa/keygen",n=n)
# chiffre=rep['ciphertext']
# m=pow(chiffre,d,n)
# i = int("0x"+str(m), base=16)
# kk = m.to_bytes(len(str(m)), byteorder='big')
# print(kk)
