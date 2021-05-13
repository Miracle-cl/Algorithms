#include <iostream>
#include <vector>
#include <climits>

using std::vector;

class Solution {
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        int dp[1+target][1+m][n];

        for (int k = 0; k <= target; ++k) {
            for (int i = 0; i <= m; ++i) {
                for (int j = 0; j < n; ++j)
                    dp[k][i][j] = INT_MAX;
            }
        }

        // vector<vector<vector<int>>> dp(1+target, vector<vector<int>>(1+m, vector<int>(n, INT_MAX)));

        for (int j = 0; j < n; ++j) {
            dp[0][0][j] = 0;
            for (int i = 1; i <= m; ++i) {
                dp[0][i][j] = INT_MAX;
            }
        }

        for (int k = 1; k <= target; ++k) {
            for (int i = k; i <= m; ++i) {
                int ci = houses[i - 1] - 1;
                if (ci >= 0) {
                    for (int j = 0; j < n; ++j) {
                        dp[k][i][j] = INT_MAX;
                        if (j == ci) {
                            for (int pre_j = 0; pre_j < n; ++pre_j)
                                dp[k][i][j] = std::min(dp[k][i][j], dp[k - (pre_j != j)][i-1][pre_j]);
                        }
                    }
                }
                else {
                    for (int j = 0; j < n; ++j) {
                        dp[k][i][j] = INT_MAX;
                        for (int pre_j = 0; pre_j < n; ++pre_j) {
                            dp[k][i][j] = std::min(dp[k][i][j], dp[k - (pre_j != j)][i-1][pre_j]);
                        }
                        if (dp[k][i][j] < INT_MAX)
                            dp[k][i][j] += cost[i-1][j];
                    }
                }
            }
        }

        int ans = INT_MAX;
        for (int j = 0; j < n; ++j) {
            ans = std::min(ans, dp[target][m][j]);
        }
        return ans == INT_MAX ? -1 : ans;
    }
};


int main()
{
    vector<int>houses {0,0,0,0,0};
    vector<vector<int>> cost {{1, 10}, {10, 1}, {10, 1}, {1, 10}, {5, 1}};
    int m = 5, n = 2, target = 3;
    Solution sol;
    int res = sol.minCost(houses, cost, m, n, target);
    std::cout << res << '\n';
    return 0;
}