#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sqlite3

## Chemin vers la base
SQLITE_DATABASE = '/chemin/vers/la/base'

## Connexion à la base
conn = sqlite3.connect(SQLITE_DATABASE)
c = conn.cursor()

#############
## Exemple 1
## Requête avec un résultat attendu de plusieurs lignes
query = 'SELECT id, nom FROM Axe'

## Exécution de la requête
c.execute(query)

## Parcours des résultats
for (att_id, att_nom) in c.fetchall():
    print 'Axe {} : {}'.format(att_id, att_nom.encode('utf-8'))

    
#############
## Exemple 2
## Requête avec un résultat attendu d'une seule ligne
query = 'SELECT COUNT(*) FROM Axe'

## Exécution de la requête
c.execute(query)

## Récupération du résultat
(count,) = c.fetchone()

print('\nNombre total d\'axes : {}'.format(count))

