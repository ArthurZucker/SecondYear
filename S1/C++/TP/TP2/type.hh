#ifndef _TYPE_HH_
#define _TYPE_HH_
#include <iostream>
enum ThreeVal_t {T='T',F='F',U='U'};
bool is_in(int *tab, const int size, const int to_find);
std::ostream & operator<<(std::ostream &os, ThreeVal_t val);
#endif