#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sqlite3

## Chemin vers la base
SQLITE_DATABASE = './sncf.db'

## Connexion à la base
conn = sqlite3.connect(SQLITE_DATABASE)
c = conn.cursor()

def exemple1():
	#############
	## Exemple 1
	## Requête avec un résultat attendu de plusieurs lignes
	query = 'SELECT G.code_UIC, G.intitule FROM GARE G where G.departement = "Aude"'

	## Exécution de la requête
	c.execute(query)

	## Parcours des résultats
	for (att_id, att_nom) in c.fetchall():
		print('{} : {}'.format(att_id, att_nom.encode('utf-8')))
	return

## Recuperation des coordonnees d’une gare a partir 
## d’une connexion a la base et du nom de la gare 
def get_gare_info(database_cursor , gare_name):
	query = 'SELECT G.longitude, G.latitude from gare G where G.intitule = \'' + gare_name + '\''
	c.execute(query)
	## Récupération du résultat
	(longe,lat) = c.fetchone()
	return (lat,longe)



if __name__ == "__main__":
	print(get_gare_info(c,str(sys.argv[1])))