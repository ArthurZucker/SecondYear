#ifndef __MOLECULE_H__
#define __MOLECULE_H__
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

class Molecule {
private:
  std::vector<std::string> forme_eclatee;
public:
  Molecule (std::string s);
  ~Molecule (){};
  std::string normalize() const;
  friend std::ostream& operator<<(std::ostream& os, const Molecule& dt);  
};
#endif
