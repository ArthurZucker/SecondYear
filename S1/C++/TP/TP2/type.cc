#include "type.hh"
std::ostream & operator<<(std::ostream &os, ThreeVal_t val)
{
	if (val == T)
	{
		os << 'T';
	}
	else if (val == F)
	{
		os << 'F';
	}
	else
	{
		os << 'U';
	}
	return os;
}
bool is_in(int *tab,const int size, const int to_find)
{
	for (size_t i = 0; i < size; i++)
	{
		if (tab[i] == to_find)
		{
			return true;
		}
	}
	return false;
}