#ifndef _EXPLOG_HH_
#define _EXPLOG_HH_
#include <string>
#include <iostream>
#include "type.hh"
class ExpLog{
public:
  virtual std::string toString() const  = 0;
  virtual ThreeVal_t evaluate()  const = 0;
  virtual ~ExpLog(){};
  bool operator==(ExpLog &A){
    return (*this).evaluate()==A.evaluate();
  }
  bool operator==(ThreeVal_t A){
    return (*this).evaluate()==A;
  }
};


#endif