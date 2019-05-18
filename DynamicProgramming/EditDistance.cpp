#include <iostream>
#include <string>

using std::string;

// https://www.dreamxu.com/books/dsa/dp/edit-distance.html
// 用分治的思想解决比较简单，将复杂的问题分解成相似的子问题
// d[i][j] : edit_distance between w1[:i] and w2[:j]
// calculated by w1[i] and w2[j]

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        int dp[n+1][m+1];
        // initialize first row and column
        for (int i = 0; i <= m; i++)
            dp[0][i] = i;
        for (int i = 1; i <= n; i++)
            dp[i][0] = i;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (word1[j-1] == word2[i-1])
                    dp[i][j] = dp[i-1][j-1];
                else
                    dp[i][j] = std::min(dp[i-1][j-1], std::min(dp[i][j-1], dp[i-1][j])) + 1;
            }
        }
        return dp[n][m];
    }
};

int main()
{
    string w1 ("horse");
    string w2 ("ros");
    Solution s;
    int res = s.minDistance(w1, w2);
    std::cout << res << std::endl;
    return 0;
}
