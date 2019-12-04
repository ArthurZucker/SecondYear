#ifndef _EXPBIN_HH_
#define _EXPBIN_HH_
#include "ExpLog.hh"
class ExpBin:public ExpLog
{
protected:
	ExpLog &op1;
	ExpLog &op2;
public:
	ExpBin(ExpLog &op,ExpLog &op1);
	virtual ~ExpBin();
	virtual std::string toString() 	const = 0;
  	virtual ThreeVal_t 	evaluate()	const = 0;
};
#endif