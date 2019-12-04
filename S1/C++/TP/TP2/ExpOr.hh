#ifndef  _EXPOR_HH_
#define  _EXPOR_HH_
#include "ExpBin.hh"
#include <string>
class ExpOr:public ExpBin
{
private:
	/* data */
public:
	ExpOr(ExpLog &A, ExpLog &B);
	~ExpOr();
	ThreeVal_t  evaluate() const;
	std::string toString() const { return("("+op1.toString()+"OR" + op2.toString() + ")");}
};
#endif