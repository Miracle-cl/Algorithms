#include <iostream>
#include <vector>
#include <algorithm>


using std::vector;


class Solution {
public:
    int maxProfit(vector<int>& inventory, int orders) {
        long long mode = 1000000007;
        int l = 0;
        int r = *std::max_element(inventory.begin(), inventory.end());
        while (l < r) {
            int T = (l + r) / 2;
            long long sum = subSum(inventory, T);
            if (sum > orders)
                l = T + 1;
            else
                r = T;
        }

        long long ans = 0;
        for (int ai : inventory) {
            if (ai >= l) {
                ans += rangeSum(l+1, ai);
                orders -= ai - l;
            }
        }
        ans += (long long) orders * l;
        
        return ans % mode;
    }

    long long subSum(const vector<int>& inventory, int thred) {
        long long ans = 0;
        for (int ai : inventory) 
            ans += ai >= thred ? ai - thred : 0;
        return ans;
    }

    long long rangeSum(int i, int j) {
        // std::cout << i << ' ' << j << '\n';
        // static_cast<long long>
        return (long long) (i + j) * (j - i + 1) / 2;
    }
};


int main () 
{
    vector<int> inventory {1000000000};
    int orders = 1000000000;
    // vector<int> inventory {2,8,4,10,6};
    // int orders = 20;
    Solution solu;
    int res = solu.maxProfit(inventory, orders);
    std::cout << res << '\n';
    return 0;
}
