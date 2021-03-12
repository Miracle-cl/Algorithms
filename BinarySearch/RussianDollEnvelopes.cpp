#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;


class Solution {
public:
    int maxEnvelopes_0(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) return 0;
        std::sort(envelopes.begin(), envelopes.end());
        int maxl = 1, n = envelopes.size();
        int dp[n];
        dp[0] = 1;
        for (int i = 1; i < n; ++i) {
            dp[i] = 1;
            for (int j = 0; j < i; ++j) {
                if (envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1])
                    dp[i] = std::max(dp[i], dp[j] + 1);
            }
            maxl = std::max(maxl, dp[i]);
        }
        return maxl;
    }

    int maxEnvelopes_1(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) return 0;
        std::sort(envelopes.begin(), envelopes.end(), [](auto& v1, auto& v2) {
            return (v1[0] < v2[0]) || (v1[0] == v2[0] && v1[1] > v2[1]);
        });
        int maxl = 1, n = envelopes.size();
        int dp[n];
        dp[0] = 1;
        for (int i = 1; i < n; ++i) {
            dp[i] = 1;
            for (int j = 0; j < i; ++j) {
                if (envelopes[j][1] < envelopes[i][1])
                    dp[i] = std::max(dp[i], dp[j] + 1);
            }
            maxl = std::max(maxl, dp[i]);
        }
        return maxl;
    }

    int maxEnvelopes_2(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) return 0;
        std::sort(envelopes.begin(), envelopes.end(), [](auto& v1, auto& v2) {
            return (v1[0] < v2[0]) || (v1[0] == v2[0] && v1[1] > v2[1]);
        });

        vector<int> increase_seq {envelopes[0][1]};
        for (int i = 1; i < envelopes.size(); ++i) {
            if (envelopes[i][1] > increase_seq.back()) {
                increase_seq.emplace_back(envelopes[i][1]);
            }
            else {
                int insert_id = std::lower_bound(increase_seq.begin(), increase_seq.end(), envelopes[i][1]) - increase_seq.begin();
                increase_seq[insert_id] = envelopes[i][1];
            }
        }
        return increase_seq.size();
    }
};


int main()
{
    vector<vector<int>> envelopes {{5,4},{6,9},{6,7},{2,3}};
    Solution sol;
    int res = sol.maxEnvelopes_2(envelopes);
    std::cout << res << '\n';
    return 0;
}