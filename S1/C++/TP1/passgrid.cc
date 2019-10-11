#include "passgrid.hh"
#include <iostream>
#include <string>

//Constructor
PassGrid::PassGrid(std::size_t w, std::size_t h):width(w),height(h){
	grid = new char*[w];
	for (size_t i = 0; i < w; i++)
	{
		grid[i] = new char[h];
		for (size_t j = 0; j < h; j++)
		{
			grid[i][j] = (rand()%61) +33;
		}
	}

}

//Destructor
PassGrid::~PassGrid(){
	for (size_t i = 0; i < width; i++)
	{
		delete[] grid[i];
	}
	delete[] grid;
}
// Function members
void PassGrid::print() const{
	std::string line(width*3-3,'-');
	line = '+' + line  + '+';
	std::cout<<line << std::endl;
	for (size_t i = 0; i < width; i++)
	{
		std::cout<<'|';
		for (size_t ii = 0; ii < height; ii++)
		{
			std::cout<<grid[i][ii]<<"|";
		}

		std::cout<<std::endl;
	}
	std::cout<<line << std::endl;

}

void PassGrid::reset(){
	for (size_t i = 0; i < width; i++)
	{
		for (size_t j = 0; j < height; j++)
		{
			grid[i][j] = (rand()%61) +33;
		}
	}
}
std::string PassGrid::generate(Path P){
	std::string out = "";
	int current_x = P.get_origin()[0];
	int current_y = P.get_origin()[1];
	for (int i = 0; i < P.get_length(); i++)
	{
		int move = P.get_path(i);
		std::cout<< grid[current_x][current_y];
		current_x += P.get_dir(move)[0];
		current_y += P.get_dir(move)[1];

	}

	return out;
}
