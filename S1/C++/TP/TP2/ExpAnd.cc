#include "ExpAnd.hh"
#include "ExpNot.hh"
#include <cstdlib>
#include <vector>
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
ExpAnd::~ExpAnd()
{
}
ExpAnd::ExpAnd(ExpAnd &A) : ExpBin(A.op1, A.op2)
{
}
CNF::~CNF()
{
	for (int i = 0; i < tabexp.size(); i++)
	{
		std::cout << "CNF destructor"<<i << std::endl;
		delete (tabexp[i]);
	}
	tabexp.clear();
	for (int i = 0; i < tabotherexp.size(); i++)
	{
		delete (tabotherexp[i]);
	}
	tabotherexp.clear();
	
	//delete myExp;
}
CNF::CNF(std::string &myfile)
{
	std::ifstream f;
	int nbvar(0);
	int *tab;
	int eval(0);
	int cpt(0);
	int cpt2(0);
	ExpLog *F1;
	ExpLog *F2;
	ExpLog *op1;
	ExpLog *op2;
	std::string read;
	f.open(myfile);
	while (std::getline(f, read))
	{

		if (read[0] != 'c')
		{
			nbvar = (int)read[6] - 48;
			tab = new int[nbvar]{};
			tabexp.reserve(nbvar);
			//tabexp = new ExpLog *[nbvar];
			break;
		}
	}
	while (f >> eval)
	{
		if (eval != 0)
		{
			if (tab[std::abs(eval) - 1] == 0)
			{
				tab[std::abs(eval) - 1] = 1;
				if (cpt == 0)
				{
					op1 = new Atom();
					//tabexp[std::abs(eval) - 1] = op1;
					tabexp.push_back(op1);
					cpt++;
				}
				else
				{
					if (eval > 0)
					{
						op2 = new Atom();
						tabexp.push_back(op2);
						//tabexp[std::abs(eval) - 1] = op2;
					}
					else
					{
						op2 = new Atom();
						tabexp.push_back(op2);
						//tabexp[std::abs(eval) - 1] = op2;
						op2 = new ExpNot(*op2);
						tabotherexp.push_back(op2);
					}
					op1 = new ExpOr(*op1, *op2);
					tabotherexp.push_back(op1);
				}
			}
			else
			{
				if (cpt == 0)
				{
					if (eval > 0)
					{
						op1 = tabexp[std::abs(eval) - 1];
						cpt++;
					}
					else if (eval < 0)
					{
						op1 = new ExpNot(*tabexp[std::abs(eval) - 1]);
						tabotherexp.push_back(op1);

						cpt++;
					}
				}
				else
				{
					if (eval > 0)
					{
						op2 = tabexp[eval - 1];
					}
					else if (eval < 0)
					{
						op2 = tabexp[std::abs(eval) - 1];
						op2 = new ExpNot(*op2);

						tabotherexp.push_back(op2);
					}
					op1 = new ExpOr(*op1, *op2);
					tabotherexp.push_back(op1);
				}
			}
		}
		else
		{
			if (cpt2 == 0)
			{
				cpt2++;
				F1 = op1;
				op1 = nullptr;
				cpt = 0;
			}
			else
			{
				F2 = op1;
				op1 = nullptr;
				F1 = new ExpAnd(*F1, *F2);
				tabotherexp.push_back(F1);
				cpt = 0;
			}
		}
	}
	f.close();

	delete tab;
	myExp = F1;
}