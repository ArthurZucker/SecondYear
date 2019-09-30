#include <iostream>
#include <string>
#include <vector>
#include "adherent.h"
#include "document.h"
using namespace std;
class bibli {
private:
  vector<Adherent> list_adherents;
  vector<Document> list_documents;
  string nom;
public:
  bibli (string);
  string get_nom();
  Document get_document_list();
  Adherent get_adherent_list();
  int set_nom(string);
  int add_doc(Document);
  int add_adhe(Adherent);
  void afficher()
  void afficher_adhe();
  void afficher_doc();
  ~bibli ();
};
