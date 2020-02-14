from subprocess import Popen, PIPE, check_output
import os
# ce script suppose qu'il a affaire à OpenSSL v1.1.1
# vérifier avec "openssl version" en cas de doute.
# attention à MacOS, qui fournit à la place LibreSSL.

# en cas de problème, cette exception est déclenchée
class OpensslError(Exception):
    pass


def genpkey(nb_bits = 1024):
    """
    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:1024 > public_key
    openssl pkey -in public_key -pubout
    """
    key_file = "pub_key"
    
    args = ['openssl', 'genpkey','-algorithm','RSA', '-pkeyopt', 'rsa_keygen_bits:{}'.format(nb_bits)]
    pipeline = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    content  = pipeline.stdout.read()
    args2 = ['openssl', 'pkey','-pubout']
    pipeline2 = Popen(args2, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout1,stderr = pipeline2.communicate(content)

    args3 = ['openssl','pkey']
    pipeline3 = Popen(args3, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout2,stderr = pipeline3.communicate(content)
    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return (stdout1.decode(),stdout2.decode())

# Il vaut mieux être conscient de la différence entre str() et bytes()
# cf /usr/doc/strings.txt

def gentempkey(bsize=16):
    """
    openssl rand -base64 bsize
    """
    args = ['openssl','rand','-base64',str(bsize)]
    pipeline = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return pipeline.stdout.read()


def pkencrypt(plaintext, passphrase,enc=1):
    """
    openssl pkeyutl -encrypt -pubin -inkey
    """
    key_file = "key_file.txt"
    # prépare les arguments à envoyer à openssl
    f = open(key_file, "a")
    f.write(passphrase)
    f.close()
    if (enc==1):
        args = ['openssl', 'pkeyutl','-encrypt', '-pubin', '-inkey' ,key_file]
    else:
        args = ['openssl', 'pkeyutl','-decrypt', '-inkey' ,key_file]
    # si le message clair est une chaine unicode, on est obligé de
    # l'encoder en bytes() pour pouvoir l'envoyer dans le pipeline vers 
    # openssl
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # ouvre le pipeline vers openssl. Redirige stdin, stdout et stderr
    #    affiche la commande invoquée
    print('debug : {0}'.format(' '.join(args)))
    pipeline = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    stdout, stderr = pipeline.communicate(plaintext)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)
    os.system("rm -rf "+key_file)  
    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return stdout


def encrypt(plaintext, passphrase, cipher='aes-128-cbc'):
    """invoke the OpenSSL library (though the openssl executable which must be
       present on your system) to encrypt content using a symmetric cipher.

       The passphrase is an str object (a unicode string)
       The plaintext is str() or bytes()
       The output is bytes()

       # encryption use
       >>> message = "texte avec caractères accentués"
       >>> c = encrypt(message, 'foobar')
       
    """
    # prépare les arguments à envoyer à openssl
    pass_arg = 'pass:{0}'.format(passphrase)
    args = ['openssl', 'enc', '-' + cipher, '-base64', '-pass', pass_arg, '-pbkdf2']
    
    # si le message clair est une chaine unicode, on est obligé de
    # l'encoder en bytes() pour pouvoir l'envoyer dans le pipeline vers 
    # openssl
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # ouvre le pipeline vers openssl. Redirige stdin, stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    pipeline = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    stdout, stderr = pipeline.communicate(plaintext)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)
    
    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return stdout.decode()

def sign(plaintext,key):
    """
    openssl dgst -sha256 -sign secret_key
    """
    key_file = "key_file.txt"
    # prépare les arguments à envoyer à openssl
    f = open(key_file, "a")
    f.write(key)
    f.close()
    args = ['openssl', 'dgst', '-sha256', '-sign',key_file]

    # si le message clair est une chaine unicode, on est obligé de
    # l'encoder en bytes() pour pouvoir l'envoyer dans le pipeline vers 
    # openssl
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # ouvre le pipeline vers openssl. Redirige stdin, stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    pipeline = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    stdout, stderr = pipeline.communicate(plaintext)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)
    os.system("rm -rf "+key_file)  
    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return stdout


def decrypt(cyphertext, passphrase, cipher='aes-128-cbc'):
    """invoke the OpenSSL library (though the openssl executable which must be
       present on your system) to encrypt content using a symmetric cipher.

       The passphrase is an str object (a unicode string)
       The plaintext is str() or bytes()
       The output is bytes()

       # encryption use
       >>> message = "texte avec caractères accentués"
       >>> c = encrypt(message, 'foobar')
       
    """
    # prépare les arguments à envoyer à openssl
    pass_arg = 'pass:{0}'.format(passphrase)
    args = ['openssl', 'enc',  '-base64','-' + cipher,'-d','-pass', pass_arg,'-pbkdf2',]

    # si le message clair est une chaine unicode, on est obligé de
    # l'encoder en bytes() pour pouvoir l'envoyer dans le pipeline vers 
    # openssl
    if isinstance(cyphertext, str):
        cyphertext = cyphertext.encode('utf-8')
    
    # ouvre le pipeline vers openssl. Redirige stdin, stdout et stderr
    #    affiche la commande invoquée
    #    print('debug : {0}'.format(' '.join(args)))
    pipeline = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # envoie plaintext sur le stdin de openssl, récupère stdout et stderr
    stdout, stderr = pipeline.communicate(cyphertext)

    # si un message d'erreur est présent sur stderr, on arrête tout
    # attention, sur stderr on récupère des bytes(), donc on convertit
    error_message = stderr.decode()
    if error_message != '':
        raise OpensslError(error_message)

    # OK, openssl a envoyé le chiffré sur stdout, en base64.
    # On récupère des bytes, donc on en fait une chaine unicode
    return stdout.decode()