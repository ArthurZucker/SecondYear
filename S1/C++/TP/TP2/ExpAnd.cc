#include "ExpAnd.hh"
ThreeVal_t ExpAnd::evaluate() const
{
	if (op1.evaluate() == F)
		return F;
	else if (op1.evaluate() == T)
		return op2.evaluate();
	else
	{
		if (op2.evaluate() == F)
			return F;
		return U;
	}
}
ExpAnd::ExpAnd(ExpLog &A, ExpLog &B):ExpBin(A,B)
{
}