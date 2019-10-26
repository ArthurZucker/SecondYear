#include "catch.hpp"
#include "../passgrid.hh"
#include "../path.hh"
bool checkCases(const PassGrid &p)
{
  for (std::size_t i = 0; i < p.get_height(); i++)
    for (std::size_t j = 0; j < p.get_width(); j++)
      if (p(i, j) < 33 || p(i, j) > 94)
        return false;
  return true;
}
bool checkCases(const std::string &p1)
{
  for (std::size_t i = 0; i < p1.length(); i++)
    if (p1[i]< 33 || p1[i] > 94)
      return false;
  return true;
}
bool diff(const PassGrid &p1, const PassGrid &p2)
{
  for (std::size_t i = 0; i < p1.get_height(); i++)
    for (std::size_t j = 0; j < p1.get_width(); j++)
      if (p1(i, j) != p2(i, j))
        return true;
  return false;
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
  Path c(10,10,10);
  std::string path1 = p0.generate(c);
  SECTION("All characters are printable")
  {
    REQUIRE(checkCases(path1));
  }

  SECTION("Two successively generated paths are different")
  {
    PassGrid p1(10, 10);
    std::string path2 = p1.generate(c);
    REQUIRE(!(path1==path2));
  }
}