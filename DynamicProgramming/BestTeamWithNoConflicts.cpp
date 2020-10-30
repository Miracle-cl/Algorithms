#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::pair;


class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        // dp[i]: max score endswith _score[i]
        int n = scores.size();
        vector<pair<int, int>> sorts;
        for (int i = 0; i < n; i++) 
            sorts.emplace_back(ages[i], scores[i]);
        // sort by first elem, then second elem
        std::sort(sorts.begin(), sorts.end());
        vector<int> dp(n, 0);
        dp[0] = sorts[0].second;
        int ans = dp[0];
        for (int i = 1; i < n; i++) {
            dp[i] = sorts[i].second;
            for (int j = 0; j < i; j++) {
                if (sorts[j].second <= sorts[i].second)
                    dp[i] = std::max(dp[i], dp[j] + sorts[i].second);
            }
            ans = std::max(ans, dp[i]);
        }
        return ans;
    }
};


int main () {
    vector<int> scores{4,5,6,5};
    vector<int> ages{2,1,2,1};
    Solution solu;
    int ans = solu.bestTeamScore(scores, ages);
    std::cout << ans << '\n';
    return 0;
}