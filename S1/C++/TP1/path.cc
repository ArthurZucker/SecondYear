#include "path.hh"
#include <cstdlib>
Path::Path(int n, std::size_t w,std::size_t h){
	length = n;
	origin[0] = rand()%w;
	origin[1] = rand()%h;
	hmax = h;
	wmax = w;
	my_path = new int[n];
	int current_x = origin[0];
	int current_y = origin[1];
	int i = 0;
	while(i<n){
		int dir = rand()%8;
		const int *move = get_dir(dir);
		if ((current_x + move[0] >= 0)  && (current_x + move[0] < w)  && (current_y + move[1] >= 0) && (current_y + move[1] < h)){
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
	for (size_t i=0;i<length-1;i++){
		std::cout << direction_human[i] << '-';
	}
	std::cout << direction_human[length]<<std::endl;
	return;
}
Path::~Path()
{
	delete[] my_path;
}

int Path::get_length() const{
	return length;
}
int* Path::get_origin() {
	return origin;
}
int Path::get_path(int i) const{
	return my_path[i];
}
const int* Path::get_dir(int i) const{
	return direction[i];
}