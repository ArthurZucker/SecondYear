#include <iostream>
#include <string>
#include <iomanip>
#include <numeric>
#include <vector>
int main(int argc, char const *argv[])
{
    std::vector<float> grades;
    float mid_term,final,to_add;
    std::string name;
    std::cout << "Welcome to your grade computer! Please enter your name\n";
    std::cin >> name;
    
    std::cout << "Now you can enter your mid-term grade : ";
    std::cin >> std::setprecision(4) >>mid_term;
    std::cout<< "Enter yout final-term grade : ";
    std::cin >> std::setprecision(4) >>final;
    std::cout<< "Finaly enter all of your homework grades : ";
    while (1)
    {
        std::cin >> std::setprecision(4) >>to_add;
        if (std::cin.eof())
        {
            break;
        }
        else{
            grades.push_back(to_add);
        }
    }
    float mean = (0.4*mid_term + 0.6*final);
    std::cout << "Your Average grade without homeworks is : "<<std::setprecision(4)<<mean<<std::endl;
    mean += std::accumulate(grades.begin(), grades.end(), 0.0)/grades.size();
    mean/=2;
    std::cout << "Your Average grade with homeworks is : "<<std::setprecision(4)<<mean<<std::endl;
    return 0;
}
