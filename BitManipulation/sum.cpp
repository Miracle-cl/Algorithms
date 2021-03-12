#include <iostream>
#include <bitset>

class Solution {
public:
    int add(int a, int b) {
        while (b != 0) {
            int c = (unsigned int)(a & b) << 1;
            a ^= b;
            b = c;
            // std::bitset<10> bs(c);
            // std::cout << bs << '\n';
        }
        return a;
    }
};


int main()
{
    Solution sol;
    int res = sol.add(20, -7);
    std::cout << res << '\n';
    return 0;
}