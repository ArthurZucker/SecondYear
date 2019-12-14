#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Mode d'emploi :
## - Placez ce script et le fichier exemple index.html dans le même répertoire
## - Exécutez ce script : python httpserver.py
## - Vérifier le fonctionnement en allant sur localhost:8083
##    (le fichier index.html doit s'afficher).
##    En pratique, localhost est la simulation de notre serveur, sur le port 8083 indiqué ci-dessous
## - Le programme ci-dessous déclare que le répertoire cgi_bin peut contenir des scripts python exécutables. Placez donc vos scripts python qui génèrent du HTML dans un répertoire cgi_bin
## - Rendez les scripts python exécutables (chmod 777 ou par l'explorateur)
## - Un script python doit générer du HTML bien formé
import BaseHTTPServer
import CGIHTTPServer

## Création d'un serveur HTTP
httpd = BaseHTTPServer.HTTPServer(("", 8083), CGIHTTPServer.CGIHTTPRequestHandler)
## Autorisation de l'exécution de script python présents
## dans le répertoire cgi_bin
## Les scripts doivent être exécutables !
CGIHTTPServer.CGIHTTPRequestHandler.cgi_directories = ["/cgi_bin"]

## Lancement en mode démon
httpd.serve_forever()

