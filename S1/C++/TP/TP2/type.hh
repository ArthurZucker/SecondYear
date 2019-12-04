#ifndef _TYPE_HH_
#define _TYPE_HH_
#include <iostream>
enum ThreeVal_t {T='T',F='F',U='U'};
std::ostream & operator<<(std::ostream &os, ThreeVal_t val);
#endif