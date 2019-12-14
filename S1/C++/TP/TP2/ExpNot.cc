#include "ExpNot.hh"
#include "Atom.hh"
ExpNot::ExpNot(ExpLog &exp) : op(exp)
{
}
ExpNot::ExpNot(ExpNot &exp) : op(exp)
{
}
ThreeVal_t ExpNot::evaluate() const
{
	switch (op.evaluate())
	{
	case T:
		return F;
		break;
	case F:
		return T;
		break;
	default:
		return U;
		break;
	}
}
std::string ExpNot::toString() const
{
	return ("NOT" + op.toString());
}
ExpNot::~ExpNot()
{
}