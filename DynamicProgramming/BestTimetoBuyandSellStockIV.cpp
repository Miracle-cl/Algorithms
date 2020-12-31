#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2)
            return 0;
        vector<int> lp(n, 0); // left_max_profit
        vector<int> rp(n, 0); // right_max_profit
        int profit = 0;
        for (int i = 1, flag = prices[0]; i < n; i++) {
            flag = std::min(flag, prices[i]);
            lp[i] = std::max(lp[i-1], prices[i] - flag);
        }

        for (int i = n - 2, flag = prices[n-1]; i >= 0; i--) {
            flag = std::max(flag, prices[i]);
            rp[i] = std::max(rp[i], flag - prices[i]);
        }

        for (int i = 0; i < n; i++) {
            profit = std::max(profit, lp[i] + rp[i]);
        }
        print_vector(lp);
        print_vector(rp);
        return profit;
    }

    void print_vector(const vector<int>& vs) {
        for (auto x : vs) {
            std::cout << x << "  ";
        }
        std::cout << "\n";
    }
};

int main()
{
    vector<int> p {3,3,5,0,0,3,1,4};
    Solution ss;
    std::cout << ss.maxProfit(p) << "\n";
    return 0;
}
