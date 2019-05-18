#include <iostream>
#include <string>

using std::string;

class Solution {
public:
    int numDistinct(const string& s, const string& t) {
        if (t.empty())
            return 1;
        if (s.empty())
            return 0;

        int row = t.size(), column = s.size();
        int dp[row+1][column+1];
        for (int i = 0; i <= column; i++)
            dp[0][i] = 1;
        for (int i = 1; i <= row; i++)
            dp[i][0] = 0;
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= column; j++) {
                dp[i][j] = dp[i][j-1] + ( (s[j-1] == t[i-1]) ? dp[i-1][j-1] : 0 );
            }
        }
        return dp[row][column];
    }

    int numDistinct2(const string& S, const string& T) {
        vector<int> f(T.size() + 1);
        f[0] = 1;
        for (int i = 0; i < S.size(); ++i) {
            for (int j = T.size() - 1; j >= 0; --j) {
                f[j + 1] += S[i] == T[j] ? f[j] : 0;
            }
        }
        return f[T.size()];
    }

};

int main()
{
    string s ("babgbag");
    string t ("bag");
    Solution solu;
    std::cout << solu.numDistinct(s, t) << "\n";
    return 0;
}
