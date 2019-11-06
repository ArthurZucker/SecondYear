#ifndef _EXPAND_HH_
#define  _EXPAND_HH_
#include <fstream>
#include <string>
#include "ExpOr.hh"
#include "Atom.hh"
#include "ExpBin.hh"
#include "type.hh"
class ExpAnd:public ExpBin
{
private:
	/* data */
public:
	ExpAnd(ExpLog &A,ExpLog &B);
	ThreeVal_t  evaluate() const;
	inline std::string toString() const { return("("+op1.toString()+"AND" + op2.toString() + ")");}
};

ExpAnd& create(std::string &myfile);

#endif