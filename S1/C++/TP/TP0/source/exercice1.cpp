#include <iostream>
#include <string>
int main()
{
std::cout << "Comment vous appellez vous ? ";
std::string name;
std::cin >> name;
std::cout << "Salut " << name << std::endl
<< "Et quel est le votre ? ";
std::cin >> name;
std::cout << "Enchante " << name << std::endl;
return 0;
}
/*
Comment vous appellez vous ? Rolling Stones
Salut Rolling
Et quel est le votre ? Enchante Stones
*/