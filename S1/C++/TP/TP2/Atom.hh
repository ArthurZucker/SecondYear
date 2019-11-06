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
	Atom(const Atom &at);
	Atom(const ThreeVal_t at);
	Atom(const ThreeVal_t &at);
	//Destructor
	~Atom();
	//Operators
	Atom &operator=(const Atom &other);
	Atom &operator=(const ThreeVal_t other);
	Atom &operator=(const bool other);
	//member functions
	inline ThreeVal_t evaluate() const { return val; }
	std::string toString() const;
};
#endif