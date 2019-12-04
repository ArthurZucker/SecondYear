#include "reaction.hh"
#include "utility.hh"
#include <map>
#include <string>
Reaction::Reaction(std::string s)
{
  std::vector<std::string> temporary(split(s, ">"));
  std::vector<std::string> g(split(temporary[0], "+"));
  std::vector<std::string> r(split(temporary[1], "+"));
  for (size_t i = 0; i < g.size(); i++)
  {
    gauche.push_back(Molecule(g[i]));
  }
  for (size_t i = 0; i < r.size(); i++)
  {
    droite.push_back(Molecule(r[i]));
  }
}
std::ostream &operator<<(std::ostream &os, const Reaction &dt)
{
  os << dt.normalize();
  return os;
}
std::string Reaction::normalize() const
{
  std::string res = "";
  std::map<std::string, int> map_gauche;
  std::map<std::string, int> map_droite;
  for (auto &x : gauche)
  {
    map_gauche[x.normalize()]++;
  }
  for (auto &x : droite)
  {
    map_droite[x.normalize()]++;
  }
  for (auto &x : map_gauche)
  {
    if (x.second > 1)
    {
      res += std::to_string(x.second) + x.first + " + ";
    }
    else
    {
      res += x.first + " + ";
    }
  }
  res.replace(res.length() - 2, 1, ">");
  for (auto &x : map_droite)
  {
    if (x.second > 1)
    {
      res += std::to_string(x.second) + x.first + " + ";
    }
    else
    {
      res += x.first + " + ";
    }
  }
  res.replace(res.length() - 2, 1, "");
  return res;
}
