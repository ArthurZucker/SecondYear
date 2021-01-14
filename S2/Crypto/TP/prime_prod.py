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


print(c.get("/bin/hackademy"))
print(c.get("/bin/hackademy/ticket/1823"))
indic0 = c.get("/bin/hackademy/ticket/1823/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1823/attachment/indication-1")
n = (c.get("/bin/hackademy/ticket/1823/attachment/n"))
x = (c.get("/bin/hackademy/ticket/1823/attachment/x"))
post = "/bin/hackademy/exam/arith/CRT"
print(indic0,indic1)
print(c.get("/bin/hackademy/ticket/1825"))
indic0 = c.get("/bin/hackademy/ticket/1825/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1825/attachment/indication-1")
indic1 = c.get("/bin/hackademy/ticket/1825/attachment/indication-2")

"""
On vous donne une liste de k nombres [n_1, ..., n_k], qui sont
deux-à-deux premiers entre eux. On note N leur produit. On vous donne aussi une
autre liste de k nombres [x_1, ..., x_k], tels que 0 <= x_i < n_i.

Vous devez déterminer X tel que :

    0 <= X < N

et

    x_1 = X mod n_1,
       ...
    x_k = X mod n_k.

Les deux listes sont en pièce-jointe (id="n" et "x"). Quand vous aurez déterminé
la valeur de X, envoyez une requête à l'adresse :

    /bin/hackademy/exam/arith/CRT

avec un paramètre "X".
---
Il y a des indications (pj = 'indication-[01]').
[ You have new mail ]
Quand il n'y a que deux nombres, il s'agit d'une application de l'algorithme
d'Euclide étendu.

Sachant que :

    X = a mod n,
    X = b mod m,

on calcule la relation de bezout entre n et m :

    u*n + v*m = 1.

Le truc, c'est que :

    b*u*n + a*v*m = a mod n,
    b*u*n + a*v*m = b mod m. Pour résoudre plus que deux équations du type :

    X = a mod l,
    X = b mod m,
    X = c mod n,

On trouve d'abord une valeur X' qui est solution de :

    X' = a mod l,
    X' = b mod m,

Puis, on cherche X tel que :

    X = X' mod l*m,
    X = c  mod n.

Ca fonctionne pareil pour 4, 5, 6, etc. équations.
"""

"""
post = "/bin/hackademy/exam/discrete-log/primitive-root"
#p=16973503711342477120805274135165619430835938743130314432054926136585928578912660174525970168659915374359727660856827057233817677312192836048898602632666177723528093433540324359025833006067992002566412718794891266025607160515284251482242568317403493898696382741971476164339781911130801156170188729203368675405031096029001040490171163591856775940982483031628912906850898345778957570258953707546194908235407045793360264256745116018346951723960210122845670298475045087367649843749596147556564176481254188618555819016544745578842756258847255193764842219562330491104021390515564019379529467330118170590366570162451975730327
indic0 = c.get("/bin/hackademy/ticket/1818/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1818/attachment/indication-1")
indic2 = c.get("/bin/hackademy/ticket/1818/attachment/indication-2")
a = int(c.get("/bin/hackademy/ticket/1818/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1818/attachment/b"))
print(indic0,indic1,indic2)

qcourant = 1
qp = b//pow(2,394)
ll = []
lima = a-1
limb = b-1
for p in primes():
    qcourant*=p
    ll.append(p)
    if(qcourant>qp):
        break
last = generate_prime_candidate2(lima//qcourant,limb//qcourant)
while(not is_prime(qcourant*last +1)):
    print(last)
    print(int.bit_length(last))
    last = generate_prime_candidate2(last+1,limb//qcourant)
qcourant*=last
ll.append(last)
print(int.bit_length(last))
p = qcourant

y = randrange(3,20000)
temp = (p-1)//(p-1)
while(pow(y,temp,p)==1):
    y = randrange(3,200000)

g = pow(y,temp,p)

print(c.post(post,g=g,p_m_1=ll))
"""


"""
print(c.get("/bin/hackademy/ticket/1819"))
a = int(c.get("/bin/hackademy/ticket/1819/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1819/attachment/b"))
q = int(c.get("/bin/hackademy/ticket/1819/attachment/q"))

lima = (a-1)//q +1
limb = (b-1)//q -1
x = randrange(lima, limb,2)
while(not is_prime(q*x +1)):

    x = randrange(lima, limb,2)

p = x*q +1


y = randrange(2,20000000000)
temp = (p-1)//q
while(pow(y,temp,p)==1):
    y = randrange(2,20000000000)

indic0 = c.get("/bin/hackademy/ticket/1819/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1819/attachment/indication-1")
indic2 = c.get("/bin/hackademy/ticket/1819/attachment/indication-2")
print(indic0,indic1,indic2)
post = "/bin/hackademy/exam/discrete-log/given-order"
temp = (p-1)//q
print(c.post(post,p=x*q +1,g=pow(y,temp,p)))
"""

#c.post("/bin/hackademy/ticket/1817/close")
"""
a = int(c.get("/bin/hackademy/ticket/1817/attachment/a"))
b = int(c.get("/bin/hackademy/ticket/1817/attachment/b"))
indic0 = c.get("/bin/hackademy/ticket/1817/attachment/indication-0")
indic1 = c.get("/bin/hackademy/ticket/1817/attachment/indication-1")
print(indic0,indic1)
"""
# 16973503711342477120805274135165619430835938743130314432054926136585928578912660174525970168659915374359727660856827057233817677312192836048898602632666177723528093433540324359025833006067992002566412718794891266025607160515284251482242568317403493898696382741971476164339781911130801156170188729203368675405031096029001040490171163591856775940982483031628912906850898345778957570258953707546194908235407045793360264256745116018346951723960210122845670298475045087367649843749596147556564176481254188618555819016544745578842756258847255193764842219562330491104021390515564019379529467330118170590366570162451975730327

#safe prime
def safe_prime(a,b):
    for q2 in range(b//12 -11,a//12-7,-1):
        print(q2)
        if(q2%3 !=0 and q2%5 !=0 and q2%7 !=0 and q2%11 !=0 ):
            q = 6*q2 +3
            if(not is_prime(q)):
                q = 6*q2+5
                if(is_prime(q)):
                    p = 12*q2 +11
                    if(is_prime(p)):
                        return p
            else:
                p = 12*q2 +7
                if(not is_prime(p)):
                    q = 6*q2+5
                    if(is_prime(q)):
                        p = 12*q2 +11
                        if(is_prime(p)):
                            return p
                else:
                    return p

"""
q = safe_prime(a,b)
print(q)
print(c.post("/bin/hackademy/exam/prime/safe",p=q))
"""
