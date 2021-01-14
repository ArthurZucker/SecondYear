#include "molecule.hh"
#include "reaction.hh"
#include "utility.hh"
#include <iostream>
#include <string>
#include <list>
#include <fstream>
#include <map>
Molecule::Molecule(std::string s) : forme_eclatee(split(s,"- =")){
}
std::ostream& operator<<(std::ostream& os, const Molecule& dt){
  os<<dt.normalize();
  return os;
}
std::string Molecule::normalize() const{
  std::map<std::string,int> temporary;
  std::string res= "";
  for(size_t iter=0; iter < forme_eclatee.size(); ++iter){
    temporary[forme_eclatee[iter]] ++;
  }
  for (auto & x : temporary){
    if (x.second > 1)
    {
      res += x.first + std::to_string(x.second);
    }
    else
    {
      res += x.first;
    }
    
  }
  return res;
}


int main()
{
  std::cout << "*** Exercice 1 ***" << std::endl;
  std::ifstream file("molecules.txt");
  std::ofstream fout("res_normalisation.txt");
  std::list<Molecule> les_molecules;
  std::string s;
  while( file >> s)
    {
      les_molecules.push_back(Molecule(s));
    }

  for(const auto& iter : les_molecules)
     {
       fout << iter<< std::endl;
     }
  file.close();

  std::cout << "*** Exercice 2 ***" << std::endl;
  file.open("reactions.txt");
  std::ofstream fout2 ("res_normalize.txt") ;
  std::list<Reaction> lesReactions;
  while(std::getline(file,s))
    {
      if(!s.empty())
	lesReactions.push_back(Reaction(s));
    }
  for(const  auto& iter : lesReactions)
   {
     fout2<< iter<< std::endl;
   }

  file.close();
  
}
