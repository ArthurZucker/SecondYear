#include "path.hh"
#include <cstdlib>
Path::Path(int n, std::size_t h,std::size_t w){
	length = n;
	origin[0] = rand()%h;
	origin[1] = rand()%w;
	hmax = h;
	wmax = w;
	my_path = new int[n];
	std::size_t current_x = origin[0];
	std::size_t current_y = origin[1];
	int i = 0;
	while(i<n){
		int dir = rand()%8;
		const int *move =get_dir(dir);
		if ((current_x + move[0] >= 0)  && (current_x + move[0] <= h)  && (current_y + move[1] >= 0) && (current_y + move[1] <= w)){
			my_path[i] = dir;
			current_x += move[0];
			current_y += move[1];
			i++;
		}
	}

}
void Path::print() const{
	std::cout << '(' << origin[0]<<',';
	std::cout << origin[1] << ")\t";
	for (int i=0;i<length;i++){
		std::cout << direction_human[i] << '-';
	}
}
Path::~Path()
{
	delete[] my_path;
}

int Path::get_length(){
	return length;
}
int* Path::get_origin(){
	return origin;
}
int Path::get_path(int i){
	return my_path[i];
}
const int* Path::get_dir(int i){
	return direction[i];
}
