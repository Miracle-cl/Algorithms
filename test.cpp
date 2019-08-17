#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;

int main() {
    // int n;
    // std::cin >> n;
    // vector<int> a(n);
    // for (size_t i = 0; i < a.size(); ++i) {
    //   std::cin >> a[i];
    // }n
    int * p;
    int q = 10;
    p = &q;
    // (*p)++;
    ++*p;
    std::cout << *p << "\n";
    return 0;
}
