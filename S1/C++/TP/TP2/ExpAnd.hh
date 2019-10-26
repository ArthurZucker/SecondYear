#ifndef _EXPAND_HH_
#define  _EXPAND_HH_
#include "ExpBin.hh"
class ExpAnd:public ExpBin
{
private:
	/* data */
public:
	ExpAnd(ExpLog &A,ExpLog &B);
	ThreeVal_t  evaluate() const;
	inline std::string toString() const { return("("+op1.toString()+"AND" + op2.toString() + ")");}
};


#endif