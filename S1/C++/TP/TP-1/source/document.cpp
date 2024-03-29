/*
 * document.cpp
 *
 *  Created on: 25 sept. 2019
 *      Author: 3670958
 */
#include "../Headers/document.h"

Document::Document(bool prolon, int data): duree_emprunt(data),prolongeable(prolon){
	cpt++;
}

int Document::getCpt() {
	return cpt;
}

void Document::setCpt(int cpt2) {
	cpt = cpt2;
}

time_t Document::getDateEmprunt() const {
	return date_emprunt;
}

void Document::setDateEmprunt(time_t dateEmprunt) {
	date_emprunt = dateEmprunt;
}

time_t Document::getDateRetour() const {
	return date_retour;
}

void Document::setDateRetour(time_t dateRetour) {
	date_retour = dateRetour;
}

const int Document::getDureeEmprunt() const {
	return duree_emprunt;
}

bool Document::isEstEmprunte() const {
	return est_emprunte;
}

void Document::setEstEmprunte(bool estEmprunte) {
	est_emprunte = estEmprunte;
}

const string& Document::getId() const {
	return id;
}

void Document::setId(const string& id) {
	this->id = id;
}

const bool Document::isProlongeable() const {
	return prolongeable;
}

const string& Document::getTitre() const {
	return titre;
}

void Document::setTitre(const string& titre) {
	this->titre = titre;
}

