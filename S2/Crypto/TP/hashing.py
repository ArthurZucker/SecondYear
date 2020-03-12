from client import *
from openssl import *
from hashlib import sha256, md5
import random
import base64
c = Connection()
print(c.post("/bin/login",user="wilkinsonethan",password="!r3YPa7u#&"))
log  = c.get("/bin/login/CHAP")
plaintext = "wilkinsonethan" + "-" + log['challenge']
response = encrypt(plaintext,"!r3YPa7u#&")
print(c.post("/bin/login/CHAP",user = "wilkinsonethan",response = response))
c.post("/bin/jukebox/disable")
c.post("/bin/jukebox/stop")


def get_stp(K,adess):
        dict = {'method':'GET','url':adess}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))


def put_stp(K,adress,message):
    message = base64.b64encode(message).decode()
    dict = {'method':'PUT','url':adress,'data':message}
    jdict =json.dumps(dict)
    enc_jdict = encrypt(jdict,K)
    response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
    #return(decrypt_b64(response,K))


def post_stp(K,adress,args):
        dict = {'method':'POST','url':adress,'args':args}
        jdict =json.dumps(dict)
        enc_jdict = encrypt(jdict,K)
        response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))
        return(decrypt_b64(response,K))



def start_stp(K):
    test1 = "/bin/login/stp/handshake"
    dict = {'method':'GET','url':test1}
    jdict =json.dumps(dict)
    enc_jdict = encrypt(jdict,K)
    response = c.post_raw("/bin/gateway",base64.b64decode(enc_jdict))



nonce = c.post("/bin/login/stp",username="shane90")
K = "means"+'-'+nonce
start_stp(K)



def create_hashed(K,i=0,username = "shane90"):
    if(i==0):
        os.system("./md5_collider/coll_finder ./md5_collider/prefix2.bin ./md5_collider/output1.bin ./md5_collider/output2.bin")
        os.system("cat ./md5_collider/prefix2.bin ./md5_collider/output1.bin > ./md5_collider/prefix3.bin")
        os.system("./md5_collider/coll_finder ./md5_collider/prefix3.bin ./md5_collider/output3.bin ./md5_collider/output4.bin")
        os.system("cat  ./md5_collider/prefix2.bin ./md5_collider/output1.bin ./md5_collider/output3.bin ./md5_collider/suffixe.bin > ./md5_collider/finale1.bin")
        os.system("cat  ./md5_collider/prefix2.bin ./md5_collider/output1.bin ./md5_collider/output4.bin ./md5_collider/suffixe.bin > ./md5_collider/finale2.bin")
        os.system("cat  ./md5_collider/prefix2.bin ./md5_collider/output2.bin ./md5_collider/output4.bin ./md5_collider/suffixe.bin > ./md5_collider/finale3.bin")
        os.system("cat  ./md5_collider/prefix2.bin ./md5_collider/output2.bin ./md5_collider/output3.bin ./md5_collider/suffixe.bin > ./md5_collider/finale4.bin")
    with open("./md5_collider/finale1.bin","rb") as f:
        file1 = f.read()
        file1 = file1[:-1]
    with open("./md5_collider/finale2.bin","rb") as f:
        file2 = f.read()
        file2 = file2[:-1]
    with open("./md5_collider/finale3.bin","rb") as f:
        file3 = f.read()
        file3 = file3[:-1]
    with open("./md5_collider/finale4.bin","rb") as f:
        file4 = f.read()
        file4 = file4[:-1]
    put_stp(K,"/home/{}/file1.bin".format(username),file1)
    put_stp(K,"/home/{}/file2.bin".format(username),file2)
    put_stp(K,"/home/{}/file3.bin".format(username),file3)
    put_stp(K,"/home/{}/file4.bin".format(username),file4)
    return(file1,file2,file3,file4)

file1,file2,file3,file4 = create_hashed(K,1)
print(get_stp(K,"/bin/fsck"))



nonce = post_stp(K,"/bin/login/stp",{'username':"wilkinsonethan"})
K = "!r3YPa7u#&"+'-'+nonce
start_stp(K)


print(get_stp(K,"/bin/police_hq"))
print(post_stp(K,"/bin/police_hq/ticket/686/close",{}))
print(post_stp(K,"/bin/police_hq/ticket/1832/close",{}))
print(get_stp(K,"/bin/police_hq"))
