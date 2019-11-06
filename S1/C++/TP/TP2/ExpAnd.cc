#include "ExpAnd.hh"
#include "ExpNot.hh"
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
ExpAnd::ExpAnd(ExpLog &A, ExpLog &B) : ExpBin(A, B)
{
}

ExpAnd &create(std::string &myfile)
{
	std::ifstream f;
	unsigned int nbvar(0);
	unsigned int nbclause(0);
	int *tab;
	f.open(myfile, std::ios::out);
	std::string read;
	while (getline(f, read))
	{
		if (read[0] != 'c')
		{
			nbvar = read[5];
			nbclause = read[7];
			tab = new int[nbvar]{};
			break;
		}
	}
	int eval(0);
	ExpLog *op1;
	ExpLog *op2;
	while (f >> eval)
	{
	}

	f.close();
}