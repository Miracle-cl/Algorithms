#include <iostream>
#include <vector>


using std::vector;


class Solution {
public:
    int minimumTimeRequired(vector<int>& jobs, int k) {
        // if work_time is known, then need dp[i] workers in state i at least
        // As work_time up, dp[i] down (worker num down)
        // dp[i] = min(dp[i-s] + 1 for s in subset of i if tot[s] <= wt)
        int n = jobs.size();
        int states = 1 << n;
        int tot[states];
        tot[0] = 0;
        for (int i = 1; i < states; i++) {
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 0) continue;
                tot[i] = tot[i - (1 << j)] + jobs[j];
                break;
            }
        }

        int l = 0, r = tot[states-1];
        while (l < r) {
            int limit = (l + r) / 2;
            int dp[states];
            dp[0] = 0;
            for (int i = 1; i < states; i++) {
                dp[i] = k+1;
                for (int s = i; s > 0; s = (s-1) & i) {
                    if (tot[s] <= limit) 
                        dp[i] = std::min(dp[i], dp[i-s] + 1);
                }
            }
            if (dp[states-1] > k)
                l = limit + 1;
            else
                r = limit;
        }
        return l;
    }

    int minimumTimeRequired_1(vector<int>& jobs, int k) {
        int n = jobs.size();
        int states = 1 << n;

        // tot[i]: time cost of job stats i
        // vector<int> tot(states, 0);
        int tot[states];
        tot[0] = 0;
        for (int i = 1; i < states; i++) {
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 0) continue;
                tot[i] = tot[i - (1 << j)] + jobs[j];
                break;
            }
        }

        // dp[j][i]: time cost of first j workers & job stats i
        // dp[j][i] = min(max(dp[j-1][i-s], tot[s]) for s in [subset of i])
        int limit = tot[states-1];
        // vector<vector<int>> dp(k, vector<int>(states, limit));
        int dp[k][states];
        for (int i = 0; i < states; i++) {
            dp[0][i] = tot[i];
        }
        for (int j = 1; j < k; j++) {
            for (int i = 0; i < states; i++) {
                dp[j][i] = limit;
                for (int s = i; s > 0; s = (s-1) & i) {
                    dp[j][i] = std::min(dp[j][i], std::max(dp[j-1][i-s], tot[s]));
                }
            }
        }
        return dp[k-1][states-1];
    }
};


int main () 
{
    vector<int> jobs {1,2,4,7,8};
    int k = 2;

    Solution sol;
    int ans = sol.minimumTimeRequired(jobs, k);
    std::cout << ans << '\n';
    return 0;
}
