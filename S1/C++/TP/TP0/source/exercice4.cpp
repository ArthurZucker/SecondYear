#include <iostream>
#include <string>
#include <iomanip>
#include <numeric>
#include <vector>
#include <fstream>
int main(int argc, char const *argv[])
{
    std::fstream file,file2;
    std::string prenom;
    int cpt=0;
    file.open("../txt/travail.txt",std::fstream::in);
    while (file.get())
    {
        if (file.eof())
        {
            file.close();
            break;
        }
        
        cpt++;
    }
    std::cout << cpt << std::endl;
    file2.open("../txt/prenomA.txt",std::fstream::out);
    file2.close();
    file.open("../txt/prenom.txt",std::fstream::in);
    while(file >> prenom)
    {
        
        std::size_t found = prenom.find_first_of('A');
        if (found != std::string::npos)
        {
            file2.open("../txt/prenomA.txt",std::fstream::app);
            file2 << prenom << std::endl;
            file2.close();
        }
        if (std::cin.eof())
        {
            file.close();
            break;

        }
        
        
       
    }
    
    

    return 0;
}
