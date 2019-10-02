#include <iostream>
#include <string>
int main(int argc, char const *argv[])
{
    int n; 
    float y;
    std::cout << "Donnez un entier et un flottant"<<std::endl;
    std::cin >> n >> y;
    std::cout << "Le produit de " << n  << " par " <<  y <<std::endl << "est : " << n*y;
    return 0;
}
