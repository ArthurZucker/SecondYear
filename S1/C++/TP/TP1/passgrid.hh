#ifndef __PASSGRID_HH_
#define __PASSGRID_HH_

#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

#include "data.hh"
#include "path.hh"
class PassGrid{
 public:
  // Constructor
  PassGrid(std::size_t w, std::size_t h);
  PassGrid(PassGrid const &P);
  // Destructor
  ~PassGrid();
  //operators
  char operator() (int i, int j) const;
  // Getters
  inline std::size_t get_height() const{
	  return height;
  }
  inline std::size_t get_width() const{
	  return width;
  }
  // Function members
  void print() const;
  std::string generate(const Path & c);
  void reset();
  void write(const std::string&);
 private:
  //attributes
  const std::size_t width;
  const std::size_t height;
  char** grid;
};

#endif