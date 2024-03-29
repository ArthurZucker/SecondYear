#ifndef ADHERENT_h
#define ADHERENT_h
#include <iostream>
#include <string>
#include <vector>
#include "document.h"
using namespace std;
class Adherent {
private:
  string prenom,nom;
  vector<Document> list_doc;
public:
  Adherent (string);
  string get_nom();
  string get_prenom();
  void set_nom(string);
  void set_prenom(string);
  vector<Document> get_doc();
  bool emprunter(Document);
  bool emprunter(string);
  bool rendre(Document);
  bool rendre(string);
  friend ostream & operator<<(ostream &os, const Adherent &Adherent ) ;
  virtual ~Adherent (){};
};
#endif
