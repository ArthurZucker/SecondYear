#ifndef _EXPNOT_HH__
#define _EXPNOT_HH__
#include "ExpLog.hh"
#include "Atom.hh"
class ExpNot : public ExpLog
{
private:
	ExpLog &op;

public:
	ExpNot(ExpLog &par);
	ExpNot(ExpNot &);
	~ExpNot();
	ThreeVal_t evaluate() const;
	std::string toString() const;
};

#endif