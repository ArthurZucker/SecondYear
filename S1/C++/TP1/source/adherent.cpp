#include "../Headers/adherent.h"

Adherent::Adherent(string allocator) {
}

string Adherent::get_nom() {
	return(nom);
}

string Adherent::get_prenom() {
	return(prenom);
}

void Adherent::set_nom(string allocator) {
	nom = allocator;
}

void Adherent::set_prenom(string allocator) {
	prenom = allocator;
}

vector<Document> Adherent::get_doc() {
	return list_doc;
}

bool Adherent::emprunter(Document document) {
	return 1;
}

bool Adherent::emprunter(string allocator) {
	return 1;
}

bool Adherent::rendre(Document document) {
	return 1;
}

bool Adherent::rendre(string allocator) {
	return 1;
}

ostream & operator<<( ostream &os, const Adherent &Adherent )
 {
	os << "Nom:" << Adherent.nom << "\nPrenom" << Adherent.prenom << "\n Etc flemme";
     return ( os ) ;
 }
