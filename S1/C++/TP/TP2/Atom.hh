#ifndef _ATOM_HH__
#define _ATOM_HH__
#include "ExpLog.hh"
#include "type.hh"
class Atom : public ExpLog
{
private:
	std ::string name;
	ThreeVal_t val;
	static int id;

public:
	//constructors
	Atom();
	Atom(Atom &at);
	Atom(ThreeVal_t at);
	Atom(ThreeVal_t &at);
	//Destructor
	~Atom();
	//Operators
	Atom &operator=(Atom &other);
	Atom &operator=(ThreeVal_t other);
	Atom &operator=(bool other);
	//member functions
	inline ThreeVal_t evaluate() const { return val; }
	std::string toString() const;
};
#endif