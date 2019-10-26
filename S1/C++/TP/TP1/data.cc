#include "data.hh"
namespace{
std::random_device device;
std::mt19937 generator(device());
std::uniform_int_distribution<unsigned int> distribution(0, INFINITY);
} // namespace

unsigned int alea::dice(){
	return distribution(generator);
}