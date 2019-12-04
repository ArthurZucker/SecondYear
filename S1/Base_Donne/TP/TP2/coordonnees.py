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
def taux_regularite(database_cursor,mois,arrive,depart):

	query = 'SELECT count(*) from \
	regularite r join Gare G, Gare G2 on G.code_UIC = r.arrivee  and G.intitule = \'' + arrive +'\' \
	and G2.code_UIC = R.depart and G2.intitule = \'' + depart +'\' \
	and r.mois = \'' + mois + '\' and r.trains_retardes <> 1 and  r.trains_annules <>  1\
	and r.trains_programmes = 1'
	
	#query = 'SELECT count(*) from regularite r join Gare G on G.code_UIC = r.arrivee  and G.intitule = \'' + arrive +'\' and r.mois = \'' + mois + '\' and r.trains_retardes <> 1 and  r.trains_annules <> 0'
	c.execute(query)
	## Récupération du résultat
	(nb,) = c.fetchone()
	query2 = 'SELECT count(*) from \
	regularite r join Gare G, Gare G2 on G.code_UIC = r.arrivee  and G.intitule = \'' + arrive +'\' \
	and G2.code_UIC = R.depart and G2.intitule = \'' + depart +'\' \
	and r.mois = \'' + mois + '\'  \
	and r.trains_programmes = 1'
	c.execute(query2)
	## Récupération du résultat
	(nb2,) = c.fetchone()
	return (nb/nb2)



if __name__ == "__main__":
	print(taux_regularite(c,"2017-05",str(sys.argv[1]),str(sys.argv[2])))