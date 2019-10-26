#include "catch.hpp"
#include <iostream>
#include "type.hh"
#include "Atom.hh"
#include "ExpNot.hh"
#include "ExpAnd.hh"
#include "ExpOr.hh"
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
  if (a.toString() != "T" || b.toString() != "T" || c.toString() != "U")
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
  if (n1.evaluate != F)
  {
    return false;
  }
  if (n2.evaluate != T)
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
  if (and1.evaluate() != U || and2.evaluate() != F || or1.evaluate() != F)
  {
    return false;
  }
  return true;
}

bool testOperations()
{
  Atom a(U), b(U), c(U);
  ExpNot nota(a);
  ExpAnd and1(a, b);
  ExpAnd and2(nota, c);
  ExpAnd and3(b, c);
  ExpOr or1(and1, and2);
  ExpOr or2(or1, and3);

  cout << or2.toString() << endl;

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
  cout << or2.toString() << endl;
  return true;
}
TEST_CASE("1: Size of the grid", "[grid]")
{
  PassGrid p0(0, 0);
  REQUIRE(p0.get_width() == 0);
  REQUIRE(p0.get_height() == 0);
  PassGrid p1(10, 8);
  REQUIRE(p1.get_width() == 10);
  REQUIRE(p1.get_height() == 8);
}

TEST_CASE("2: Grid contents", "[grid]")
{
  PassGrid p0(10, 10);
  SECTION("All characters are printable character")
  {
    REQUIRE(checkCases(p0));
  }

  SECTION("Two successively generated grid are different")
  {
    PassGrid p1(10, 10);
    REQUIRE(diff(p0, p1));
  }
  SECTION("reset make differences")
  {
    PassGrid p1(p0);
    p0.reset();
    REQUIRE(diff(p0, p1));
  }
}
TEST_CASE("3: different path", "[path]")
{
  PassGrid p0(10, 10);
  Path c(10, 10, 10);
  std::string path1 = p0.generate(c);
  SECTION("All characters are printable")
  {
    REQUIRE(checkCases(path1));
  }

  SECTION("Two successively generated paths are different")
  {
    PassGrid p1(10, 10);
    std::string path2 = p1.generate(c);
    REQUIRE(!(path1 == path2));
  }
}