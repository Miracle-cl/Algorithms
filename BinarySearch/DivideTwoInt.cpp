#include <iostream>
#include <climits>

class Solution {
public:
    int divide(int dividend, int divisor) {
        long long m = std::abs((long long) dividend);
        long long n = std::abs((long long) divisor);
        long long res = 0;

        if (m < n)
            return 0;
        while (m >= n) {
            long long t = n, p = 1;
            while (m >= (t << 1)) {
                t <<= 1;
                p <<= 1;
            }
            res += p;
            m -= t;
        }
        res = (dividend < 0) ^ (divisor < 0) ? -res : res;
        return res > INT_MAX ? INT_MAX : res;
    }
};

int main()
{
    int a = -2147483648, b = -1;

    Solution solu;
    long long res = solu.divide(a, b);
    std::cout << res << "\n";
    return 0;
}
