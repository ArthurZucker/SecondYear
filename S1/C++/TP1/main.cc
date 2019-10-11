#include <iostream>
#include <ctime>
#include "passgrid.hh"
#include "path.hh"
// There are no momory leap, but the heap has a "still reachable" part, which is a BUG
// from Valgrind and C++ istefl, stated on stackoverflow
int main(int argc, char **argv)
{
  std::string file_name = argv[1];
  srand(time(NULL));
  PassGrid pg(4,5);
  pg.print();
  pg.reset();
  std::cout << std::endl;
  pg.print();
  Path c(5,4,5);
  c.print();
  std::cout << std::endl;
  std::cout<< pg.generate(c) << std::endl;
  pg.write(file_name);
}
