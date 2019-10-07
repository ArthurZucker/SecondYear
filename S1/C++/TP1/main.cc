#include <iostream>

#include "passgrid.hh"
#include "path.hh"

int main()
{
  PassGrid pg(4,5);
  pg.print();
  pg.reset();
  std::cout << std::endl;
  pg.print();
  Path c(5,4,5);
  c.print();
  std::cout<< pg.generate(c) << std::endl;
}
