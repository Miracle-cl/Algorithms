#include <iostream>
#include <string>

using std::string;

class Solution
{
public:
    int minCut(const string& s) {
        int lens = s.size();
        int dp[lens+1];
        bool P[lens][lens];

        for (int i = 0; i <= lens; i++)
            dp[i] = lens - i - 1;

        for (int i = 0; i < lens; i++) {
            for (int j = 0; j < lens; j++)
                P[i][j] = false;
        }

        for (int i = lens - 1; i >= 0; i--) {
            for (int j = i; j < lens; j++) {
                if (s[i] == s[j] && (j - i <= 1 || P[i+1][j-1])) {
                    P[i][j] = true;
                    dp[i] = std::min(dp[i], dp[j+1]+1);
                }
            }
        }
        return dp[0];
    }
};

int main()
{
    string str ("abcbabaa");
    Solution s;
    std::cout << s.minCut(str) << "\n";
    return 0;
}
