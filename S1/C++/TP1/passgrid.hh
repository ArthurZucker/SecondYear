#pragma once
#include <cstdlib>
#include "path.hh"
#include <string>
#include <vector>
class PassGrid{
 public:
  // Constructor
  PassGrid(std::size_t w, std::size_t h);
  // Destructor
  ~PassGrid();
  // Function members
  void print() const;
  std::string generate(Path);
  void reset();
  // Getters
  std::size_t get_height();
  std::size_t get_width();
  char** get_grid();
  // Setters
  void set_height();
  void set_width();
  void set_case(int,int);
 private:
  //attributes
  const std::size_t width;
  const std::size_t height;
  const int direction[8][2]={{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,1},{1,-1}};
  char** grid;
};
