#include "ExpOr.hh"
ThreeVal_t ExpOr::evaluate() const
{
	if (op1.evaluate()==T)
		return T;
	else if (op1.evaluate()==F)
		return op2.evaluate();
	else
	{
		if (op2.evaluate()==T)
			return T;
		return U;
	}
}
ExpOr::ExpOr(ExpLog &A, ExpLog &B):ExpBin(A,B)
{

}
