#include <iostream>
#include <string>
#include <vector>
#include <time>
using namespace std;
class Document {
private:
  int const duree_emprunt;
  static int cpt;
  string id;
  string titre;
  bool est_emprunte;
  bool const prolongeable;
  time_t date_emprunt;
  time_t date_retour;
public:
  Document (arguments);
  virtual ~Document ();
};
