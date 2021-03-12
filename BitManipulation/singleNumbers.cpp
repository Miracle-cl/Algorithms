#include <iostream>
#include <vector>

using std::vector;


class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        int x = 0;
        for (int num : nums)
            x ^= num;
        int div = 1;
        while ((div & x) == 0)
            div <<= 1;

        int a = 0, b = 0;
        for (int num : nums) {
            if ((div & num) == 0)
                a ^= num;
            else 
                b ^= num;
        }
        return {a,b};
    }
};

class SolutionII {
public:
    int singleNumber(vector<int>& nums) {
        // nums = {3,4,3,3}
        int ret = 0;
        for (int i = 0; i < 32; ++i) {
            int x = 0;
            for (int& num : nums) {
                x += (num & 1);
                num >>= 1;
            }
            x %= 3;
            if (x > 0)
                ret += x * (1 << i);
        }
        return ret;
    }
};


int main ()
{
    Solution sol;
    vector<int> nums {4,2,4,6};
    vector<int> res = sol.singleNumbers(nums);
    
    for (int x : res) {
        std::cout << x << '\n';
    }
    return 0;
}

