#ifndef  _EXPOR_HH_
#define  _EXPOR_HH_
#include "ExpBin.hh"
class ExpOr:public ExpBin
{
private:
	/* data */
public:
	ExpOr(ExpLog &A, ExpLog &B);
	ThreeVal_t  evaluate() const;
	inline std::string toString() const { return("("+op1.toString()+"OR" + op2.toString() + ")");}
};

#endif