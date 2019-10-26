#include "path.hh"

Path::Path(int n, std::size_t w, std::size_t h){
	length = n-1;
	origin[0] = alea::dice() % w;
	origin[1] = alea::dice() % h;
	hmax = h;
	wmax = w;
	my_path = new int[length];
	size_t current_x = origin[0];
	size_t current_y = origin[1];
	int i(0);
	int possible_direction(8); //Uniform initialisation
	while (i < length){
		int dir = alea::dice() % possible_direction;
		const int *move = get_dir(dir);
		if ((current_x + move[0] >= 0) && (current_x + move[0] < w) && (current_y + move[1] >= 0) && (current_y + move[1] < h)){
			my_path[i] = dir;
			current_x += move[0];
			current_y += move[1];
			i++;
		}
	}
}

void Path::print() const
{
	std::cout << '(' << origin[0] << ',';
	std::cout << origin[1] << ")\t";
	for (int i = 0; i < length ; i++){
		std::cout << direction_human[my_path[i]] << '-';
	}
	return;
}

Path::~Path(){
	delete[] my_path;
}

int Path::get_length() const{
	return length;
}

const int *Path::get_origin() const{
	return origin;
}

const int Path::get_path(const int &i) const{
	return my_path[i];
}

const int *Path::get_dir(int i) const{
	return direction[i];
}
