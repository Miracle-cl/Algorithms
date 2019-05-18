#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size(), n = s2.size(), l = s3.size();
        if (l != m + n)
            return false;
        vector<vector<bool>> dp (m+1, vector<bool>(n+1, true));
        // initialize first column
        for (int i = 1; i <= m; i++)
            dp[i][0] = dp[i-1][0] && s1[i-1] == s3[i-1];

        // initialize first row
        for (int i = 1; i <= n; i++)
            dp[0][i] = dp[0][i-1] && s2[i-1] == s3[i-1];

        // modify matrix intenel
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // left() - judge 1/0 from last row; || right() - judge 1/0 from last column
                dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
            }
        }
        // for (auto x: dp)
        //     print_vector(x);
        return dp[m][n];
    }

    void print_vector(const vector<bool>& vs) {
        for (auto x : vs) {
            std::cout << x << "  ";
        }
        std::cout << "\n";
    }
};


int main()
{
    string s1 ("aabcc");
    string s2 ("dbbca");
    string s3 ("aadbbcbcac");
    // string s3 ("aadbbbaccc");
    Solution ss;
    bool res = ss.isInterleave(s1,s2,s3);

    std::cout << res << "\n";
    return 0;
}
