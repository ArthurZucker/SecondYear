/*
 * Numeric.h
 *
 *  Created on: 25 sept. 2019
 *      Author: 3670958
 */

#ifndef HEADERS_NUMERIC_H_
#define HEADERS_NUMERIC_H_
#include "document.h"
class Numeric : public Document{
private:
	int nb_emprunter;
public:
	Numeric(bool prolo, int date);
	friend ostream & operator<<(ostream &os, const Numeric &Numeric ) ;
	int getNbEmprunter() const;
	void setNbEmprunter(int nbEmprunter);
};






#endif /* HEADERS_NUMERIC_H_ */
