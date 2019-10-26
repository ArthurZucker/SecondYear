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
