/*
 * Numeric.cpp
 *
 *  Created on: 25 sept. 2019
 *      Author: 3670958
 */
#include "../Headers/Numeric.h"

int Numeric::getNbEmprunter() const {
	return nb_emprunter;
}

Numeric::Numeric(bool prolo, int date) : Document(prolo,date){
}

void Numeric::setNbEmprunter(int nbEmprunter) {
	nb_emprunter = nbEmprunter;
}
ostream & operator<<(ostream &os, const Numeric &Numeric ){
	os << "Comment j'ai la flemme";
	return os;
}
