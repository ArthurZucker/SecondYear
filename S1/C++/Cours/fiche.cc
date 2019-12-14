// C++ courses resume and exemple explained
// namespaces
#include <iostream>
using namespace std;

namespace foo
{
int value(); //declaration
} // namespace foo
namespace bar
{
const double pi = 3.1416; // unchanged during run time
double value() { return 2 * pi; }
} // namespace bar

void increment(int &v)
{
	v++;
}

int main()
{
	using bar::value;			  //Allows us to use value() called from bar
	cout << foo::value() << endl; //Call to value in the foo namespace, returns 5
	cout << value() << endl;	  //Call to value in the bar namespace, returns 2*pi
	cout << bar::pi << endl;	  //Call to value in the foo namespace, returns pi
	//Pointers :
	int a = 3;
	int x = 5;
	int *p = &x;
	cout << "x = " << x << endl;
	cout << "p = " << p << " ; *p = " << p << endl;
	*p = 6;
	p = p + 1;
	cout << "x = " << x << endl;
	cout << "p = " << p << " ; *p = " << p << endl;
	// Const & pointers
	char greetings[] = "Hello";
	char *p0 = greetings;			  //non const pointer & non const data
	const char *p1 = greetings;		  //non const pointer & const data!
	char *const p2 = greetings;		  //const pointer		& non const data!
	const char *const p3 = greetings; //const pointer 	& const data
	// Static variables: initialized only once!
	int d(2);
	// Dynamic
	int a1 = 3;
	int *pa;
	int &ra = a1;
	pa = &a1;
	ra = 4;
	increment(a1); //Pass by reference which increments the instance
	cout << "a1= " << a1 << " &a1 = " << &a1 << endl;
	cout << "*pa = " << *pa << " pa = " << pa << endl;
	cout << "ra = " << ra << " &ra = " << &ra << endl;
	double d1;
	const double d_const = 4.0;
	double &a12 = d1;
	const double &b1 = d1;
	const double &c1 = d_const;
	const double &c_const = d_const;
	//const functions on object implies that the object on which it is called does not get changed
	int n = 4;
	const int n2 = 5;
	int (*M)[n2] = new int[n][n2];
	delete[] M;
	return 0;
}
int foo::value() { return 5; } //definition of the function