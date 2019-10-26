#include "passgrid.hh"
//constructor
PassGrid::PassGrid(std::size_t w, std::size_t h) : width(w), height(h){
	grid = new char *[w];
	for (size_t i = 0; i < w; i++){
		grid[i] = new char[h];
		for (size_t j = 0; j < h; j++){
			grid[i][j] = alea::dice() % MAX_ASKI + MIN_ASKI;
		}
	}
}

//Copy constructor
PassGrid::PassGrid(PassGrid const &P) : width(P.get_width()), height(P.get_height()){
	grid = new char *[width];
	for (size_t i = 0; i < width; i++){
		grid[i] = new char[height];
		for (size_t j = 0; j < height; j++){
			grid[i][j] = P(i, j);
		}
	}
}

// Operator added in order to pass tests
char PassGrid::operator()(int i, int j) const{
	return grid[i][j];
}

//Destructor
PassGrid::~PassGrid(){
	for (size_t i = 0; i < width; i++){
		delete[] grid[i];
	}
	delete[] grid;
}

// Function members
void PassGrid::print() const{
	std::cout << std::setfill('-') << std::setw(print_width * (width)) << "\n"
			  << std::setfill(' ');
	for (size_t i = 0; i < width; i++){
		std::cout << '|';
		for (size_t ii = 0; ii < height; ii++){
			std::cout << std::setw(print_width) << grid[i][ii] << "|";
		}
		std::cout << '\n';
	}
	std::cout << std::setfill('-') << std::setw(print_width * width) << "\n"
			  << std::setfill(' ');
}

std::string PassGrid::generate(const Path &P){
	std::string out = "";
	int current_x = P.get_origin()[0];
	int current_y = P.get_origin()[1];
	int l = P.get_length();
	int move(0);
	for (int i = 0; i < l; i++){
		move = P.get_path(i);
		out += grid[current_x][current_y];
		current_x += P.get_dir(move)[0];
		current_y += P.get_dir(move)[1];
	}
	out += grid[current_x][current_y];
	return out;
}

void PassGrid::reset(){ //not inline because it has a loop (read somewhere that you should not inline those )
	for (size_t i = 0; i < width; i++){
		for (size_t j = 0; j < height; j++){
			grid[i][j] = (alea::dice()) % MAX_ASKI + MIN_ASKI;
		}
	}
	return;
}

void PassGrid::write(const std::string &file){
	std::ofstream ff;
	ff.open("/Users/arthur/Travail/Polytech/MAIN4/S1/C++/TP/TP1/" + file);
	ff << "<?xml version='1.0' standalone='no'?>\n<!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN'\n'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>\n<svg width='100%' height='100%' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>\n";
	ff << "\n<title>Grid view</title>\n";
	ff << "<g id='rowGroup'>\n<rect x='65' y='30' width='75' height='" << height * 30 << "' fill='gainsboro'/>\n<rect x='265' y='30' width='75' height='" << height * 30 << "' fill='gainsboro'/>\n";
	ff << "\t<text x='" << 30 << "' y='" << 30 << "' font-size='18px' font-weight='bold' fill='crimson'>\n";
	for (size_t i = 0; i < height; i++){
		ff << "<tspan x='30' dy='1.5em'>" << i + 1 << "</tspan>\n";
		ff << "<line x1='" << 30 * i + 30 << "' y1='30' x2='" << 30 * i + 30 << "' y2='" << height * 30 << "' stroke='#529fca' />\n";
	}
	ff << "</text>\n";
	for (size_t i = 0; i < width; i++){
		ff << "\t<text x='" << i * 100 + 100 << "' y='" << 30 << "' font-size='18px' text-anchor='middle'>\n";
		for (size_t ii = 0; ii < height; ii++){
			if (grid[i][ii] == '&' || grid[i][ii] == '\'' || grid[i][ii] == '\"' || grid[i][ii] == '>' || grid[i][ii] == '<'){
				ff << "\t\t<tspan x='" << i * 100 + 100 << "' dy='1.5em'>"
				   << "&#" << int(grid[i][ii]) << ';' << "</tspan>\n";
			}
			else{
				ff << "\t\t<tspan x='" << i * 100 + 100 << "' dy='1.5em'>" << grid[i][ii] << "</tspan>\n";
			}
		}
		ff << "\t</text>";
	}
	ff << "</g>\n</svg>";
	ff.close();
}
