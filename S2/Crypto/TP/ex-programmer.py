from client import *
from openssl import *
import json
import base64
import time
c = Connection()
with open("jennifergriffin","r") as f:
    user = f.readline().strip('\n')
    key = f.read()
print(user)
print(key)
i =(c.get("/bin/login/passwordless"))
try:
    print(c.post("/bin/login/passwordless",user=user,response = base64.b64encode(sign(i["challenge"],key)).decode()))
except  Exception as e:
    print(e.msg)
    print(c.get("/bin/courthouse/shane90"))
    print(c.get("/bin/courthouse/{}".format(user)))

"""

Il semble que lors des procès, les magistrats envoient des requêtes à une base
de données. La dernière requête envoyée lors du procès en cours à l'air d'être
toujours accessible via une requête GET à l'adresse :

	/bin/courthouse/database


On peut aussi ***envoyer** des requêtes au serveur de base de données... mais il
y a un "mais". Les requêtes doivent être accompagnées d'un MAC pour être
considérées comme valides par le serveur de base de données. Apparemment, ce
serveur partage une clef secrète avec les magistrats, et nous ne la connaissons
pas.

Plus précisément, "on" nous a laissé regarder un document confidentiel avec les
specifications du système. Il en ressort que pour envoyer une requête à la base
de données, les greffiers envoient une requête POST avec deux arguments "query"
et "mac" à la même adresse :

	/bin/courthouse/database

Comme ils ont apparemment prévu la possibilité que la "query" puisse contenir
des données binaires, elle est donc encodée en base64.

Par ailleurs, nous connaissons aussi le code d'authentification de message
utilisé. C'est là qu'est la bonne surprise, car ils ont fait n'importe quoi. En
effet, le serveur exécute les requêtes SQL qu'il reçoit si :

    input['mac'] == SHA-256(K || Q), avec Q == base64.decode(input['query']).

où K est une clef secrète de 128 bits que nous ne connaissons pas, et où
l'opérateur || désigne comme d'habitude la concaténation.

Ceci nous donne la possibilité de ***forger*** des requêtes sans connaître la
clef K... par exemple pour faire disparaître des accusations gênantes.

Nous avons pu glaner ici et là des informations supplémentaires. Elles sont
accessibles ici :

    /knowledge-center/courthouse-hack/<i>    avec    i = 0,....

Nos amis chez les administrateurs ont mis à notre disposition leur
implémentation de SHA-256, que vous pourrez obtenir ici :

    /share/sha256.py

Votre attention est aussi attirée sur un utilitaire accessible à tous :

    /bin/sha256sum

qui fournit des informations de débuguage très pratiques.
Le code d'authentification de message est :

    mac = H(K || M),

où K est une clef de 16 octets inconnue. Par contre, M et le mac sont connus. La
fonction de hachage SHA-256 traite le message par blocs de 64 octets. Imaginons
donc le découpage :

      bloc 0         bloc 1       bloc 2

KKKMM.....MM | MMM......MMM | MMM......MMM | MM<bloc incomplet>
 ^
 |
clef

La clef occupe le quart du premier bloc. Le dernier bloc, incomplet, va être
rempli par le mécanisme de bourrage. La ruse, c'est qu'on peut prédire ce qui va
être ajouté au dernier bloc, car on connaît la TAILLE de ce qui est haché.



"""
