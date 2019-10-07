#pragma once
#include <iostream>
#include <string>
class Path
{
private:
	int length;
	int origin[2];
	const int direction[8][2]={{-1,0},{1,0},{0,-1},{0,1},{-1,-1},{-1,1},{1,1},{1,-1}};
	const std::string direction_human[8]={{"S"},{"N"},{"E"},{"W"},{"SE"},{"SW"},{"NW"},{"NE"}};
	std::size_t hmax;
	std::size_t wmax;
	int *my_path;
public:
	Path(int n, std::size_t hmax,std::size_t wmaw);
	~Path();
	void print() const;
	int get_length();
	int* get_origin();
	const int* get_dir(int);
	int get_path(int i);
};

