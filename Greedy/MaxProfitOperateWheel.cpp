#include <iostream>
#include <vector>

using std::vector;


class Solution {
public:
    int minOperationsMaxProfit(vector<int>& customers, int boardingCost, int runningCost) {
        if (boardingCost * 4 <= runningCost)
            return -1;
        int max_ = INT8_MIN, profit = 0, turns = -1, waiting = 0;
        int n = customers.size();
        for (int i = 0; i < n; i++) {
            waiting += customers[i];
            if (waiting <= 0)
                profit -= runningCost;
            else if (waiting < 4) {
                profit += boardingCost * waiting - runningCost;
                waiting = 0;
            }
            else {
                // waiting > 4
                profit += boardingCost * 4 - runningCost;
                waiting -= 4;
            }

            if (profit > max_) {
                max_ = profit;
                turns = i + 1;
            }
        }
        // std::cout << max_ << waiting << turns << "\n";
        if (waiting > 0) {
            int _t = waiting / 4;
            int p1 = profit + boardingCost * _t * 4 - runningCost * _t;
            int p2 = profit + boardingCost * waiting - runningCost * (_t + 1);
            if (p2 > p1 && p2 > max_) {
                turns = n + _t + 1; // max_ = p2
                max_ = p2;
            }
            else if (p1 > max_) {
                turns = n + _t; // max_ = p1
                max_ = p1;
            }
        }
        return max_ > 0 ? turns : -1;
    }
};


int main() 
{
    vector<int> customers {10,10,1,0,0};
    int boardingCost = 4;
    int runningCost = 4;
    Solution solu;
    int res = solu.minOperationsMaxProfit(customers, boardingCost, runningCost);
    std::cout << res << '\n';
    return 0;
}