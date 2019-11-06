#include <iostream>
#include <ctime>
#include <chrono>

#include "passgrid.hh"
#include "path.hh"
int main(int argc, char **argv){
  auto start = std::chrono::steady_clock::now();
  if (argc<=1) {
    std::cout<<"No file name were given, please restart with a file name"<<std::endl;
    return 0;
  }
  std::string file_name = argv[1];
  PassGrid pg(8,10);
  pg.print();
  pg.reset();
  std::cout << std::endl;
  pg.print();
  Path c(10,8,10);  
  c.print();
  std::cout << std::endl;
  std::cout<< pg.generate(c) << std::endl;
  pg.write(file_name);
  auto end = std::chrono::steady_clock::now();
  std::cout<<"Time taking by your program : t = " << std::chrono::duration <double, std::milli> (end-start).count()<< " ms" << std::endl;
  return 1;
}
