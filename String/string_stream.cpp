#include <iostream>
#include <sstream>
#include <iterator>

using std::string;

int main ()
{
    // string s("3,4,66,9,,10");
    // string x;
    // std::stringstream ss(s);
    // while (std::getline(ss, x, ',')) {
    //     std::cout << x << '\n';
    // }

    string s("35, 4 \n  5");
    std::stringstream ss(s);
    // char ch;
    string ch;
    while (ss >> ch) 
        std::cout << ch << '\n';

    // string sentence("Cpp is fun");
    // std::istringstream in(sentence);
    // // char x;
    // string x;
    // while (in >> x) 
    //     std::cout << x << '\n';
    return 0;
}