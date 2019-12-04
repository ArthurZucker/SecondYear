#ifndef _EXPAND_HH_
#define _EXPAND_HH_
#include <fstream>
#include <string>
#include "ExpOr.hh"
#include "Atom.hh"
#include "ExpBin.hh"
#include "type.hh"
#include <vector>
class ExpAnd : public ExpBin
{
private:
	/* data */
public:
	ExpAnd(ExpLog &A, ExpLog &B);
	ExpAnd(ExpAnd &A);
	~ExpAnd();
	ThreeVal_t evaluate() const;
	std::string toString() const { return ("(" + op1.toString() + "AND" + op2.toString() + ")"); }
};

class CNF
{
private:
	std::vector<ExpLog *> tabexp;
	std::vector<ExpLog *> tabotherexp;
	ExpLog *myExp;

public:
	CNF(std::string &myfile);
	~CNF();
	ThreeVal_t evaluate() const { return myExp->evaluate(); };
	std::string toString() const { return ("(" + myExp->toString() + ")"); }
};
#endif