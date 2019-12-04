#include "utility.hh"


std::vector<std::string> split(const std::string& s, const std::string& s_s )
{
  std::vector<std::string> res;
  std::string phrase(s);
  std::string::size_type debutMot, finMot;
  std::string::size_type longMot;
  debutMot=0;
  while (debutMot != std::string::npos)
    {
    
      debutMot = phrase.find_first_not_of(s_s);
      finMot   = phrase.find_first_of(s_s,debutMot+1);
      longMot  = ((finMot == std::string::npos)?phrase.size():finMot) - debutMot;
      if( debutMot != std::string::npos)
	{ 
	  
	  if(!phrase.substr(debutMot,longMot).empty())
	    res.push_back(phrase.substr(debutMot,longMot));
	  phrase = phrase.substr(debutMot+longMot);
	  
	}
    }
  return res;
}
