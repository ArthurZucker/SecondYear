#include "Atom.hh"
int Atom::id = 0;
Atom::Atom() : name("a_" + std::to_string(id)), val(U)
{
	id++;
}
Atom::Atom(Atom &at) : name("a_" + std::to_string(id)), val(at.val)
{
	id++;
}
Atom::Atom(ThreeVal_t at) : name("a_" + std::to_string(id)), val(at)
{
	id++;
}
Atom::Atom(ThreeVal_t &at) : name("a_" + std::to_string(id)), val(at)
{
	id++;
}
Atom &Atom::operator=(ThreeVal_t other)
{
	val = other;
	return *this;
}
std::string Atom::toString() const
{
	std::string chaine("(" + name + "=");
	switch (val)
	{
	case T:chaine+='T';break;
	case F:chaine+='F';break;
	default:chaine+='U';break;
	}
	chaine += ")";
	return chaine;
}
Atom &Atom::operator=(bool other)
{
	if (other)
	{
		val = T;
	}
	else
	{
		val = F;
	}
	return *this;
}
Atom &Atom::operator=(Atom &other)
{
	val = other.val;
	return *this;
}
Atom::~Atom()
{
}
