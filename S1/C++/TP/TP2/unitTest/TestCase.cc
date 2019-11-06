#include "catch.hpp"
#include <iostream>
#include "../type.hh"
#include "../Atom.hh"
#include "../ExpNot.hh"
#include "../ExpAnd.hh"
#include "../ExpOr.hh"
using namespace std;
bool testAtom()
{
  Atom a(T);
  Atom b;
  Atom c(b);
  b = T;
  if (a.evaluate() != T || b.evaluate() != T || c.evaluate() != U)
  {
    return false;
  }
  c = false;
  a = b = F;
  if (a.evaluate() != F || b.evaluate() != F || c.evaluate() != F)
  {
    return false;
  }
  return true;
}

bool testExpNot()
{
  Atom a(T);
  ExpNot n1(a);
  ExpNot n2(n1);
  if (n1.evaluate() != F)
  {
    return false;
  }
  if (n2.evaluate() != T)
  {
    return false;
  }
  return true;
}

bool testExpOrExpAnd()
{
  Atom a(T);
  Atom b;
  Atom c(F);
  ExpNot n1(a);
  ExpAnd and1(n1, b);
  ExpAnd and2(c, b);
  ExpOr or1(and1, and2);
  if (and1.evaluate() != F || and2.evaluate() != F || or1.evaluate() != F)
  {
    return false;
  }
  return true;
}

bool testOperations()
{
  Atom a(U), b(U), c(U);
  ExpNot nota(a);        //U
  ExpAnd and1(a, b);     //U and U=U
  ExpAnd and2(nota, c);  //U and U=U
  ExpAnd and3(b, c);     //U and U=U
  ExpOr or1(and1, and2); // U or U = U
  ExpOr or2(or1, and3);  // U or U = U

  if (or2.evaluate() != U)
  {
    return false;
  }
  while (or2 == U)
  {
    if (a == U)
    {
      a = T;
      continue;
    }
    if (b == U)
    {
      b = T;
      continue;
    }
    if (c == U)
    {
      c = F;
      continue;
    }
  }
  if (or2.evaluate() != T)
  {
    return false;
  }
  return true;
}
TEST_CASE("1: test on atoms", "[Atoms]")
{
  REQUIRE(testAtom());
}

TEST_CASE("2: test on ExpNot", "[ExpNot]")
{
  REQUIRE(testExpNot());
}
TEST_CASE("3: test on And & Or", "[ExpBin]")
{
  REQUIRE(testExpOrExpAnd());
}

TEST_CASE("4: more operations", "[All]")
{

  SECTION("Evaluate test")
  {
    REQUIRE(testOperations());
  }

  SECTION("Threeval test")
  {
    ThreeVal_t t = T;
    ThreeVal_t t1 = F;
    ThreeVal_t t2 = U;
    REQUIRE(t == 'T');
    REQUIRE(t1 == 'F');
    REQUIRE(t2 == 'U');
  }
}