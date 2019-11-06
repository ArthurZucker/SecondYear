#ifndef _PATH_HH_
#define _PATH_HH_
#include <iostream>
#include <random>
#include <string>
#include <cstdlib>
#include "data.hh"
class Path
{
private:
	int length{0}; //initialised to avoid random behavior
	int origin[2];
	const int direction[8][2]={{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,1},{1,-1}};
	const std::string direction_human[8]={{"N"},{"S"},{"W"},{"E"},{"NW"},{"NE"},{"SE"},{"SW"}};
	std::size_t wmax{0};
	std::size_t hmax{0};
	int *my_path;
public:
	Path(int n, std::size_t hmax,std::size_t wmaw);
	~Path();
	void print() const;
	int get_length() const;
	const int* get_origin() const;
	const int* get_dir(int) const;
	const int get_path(const int &i) const;
};
#endif
