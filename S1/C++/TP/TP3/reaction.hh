#ifndef __REACTION_H__
#define __REACTION_H__
#include <vector>
#include "molecule.hh"
class Reaction {
private:
  std::vector<Molecule> gauche;
  std::vector<Molecule> droite;
public:
  Reaction (std::string chaine);
  ~Reaction (){};
  std::string normalize() const;
  friend std::ostream& operator<<(std::ostream& os, const Reaction& dt);
};



#endif
