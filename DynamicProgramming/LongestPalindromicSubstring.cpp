#include <iostream>
#include <string>
#include <vector>

using std::vector;
using std::string;

class Solution {
public:
    // method 1
    string longestPalindrome1(string s) {
        // 20 ms; 8.6 MB
        if (s.size() < 2)
            return s;
        int start = 0, max_len = 0;
        for (int i = 0; i < s.size(); i++) {
            search(i, i, start, max_len, s);
            search(i, i+1, start, max_len, s);
        }
        return s.substr(start, max_len);
    }

    void search(int left, int right, int& start, int& max_len, const string& s) {
        while (left >= 0 && right < s.size() && s[left] == s[right])
            left--, right++;
        if (max_len < right - left - 1) {
            max_len = right - left - 1;
            start = left + 1;
        }
    }

    // method 2
    string longestPalindrome2(string s) {
        // 150+ ms; 13+ MB
        if (s.size() < 2)
            return s;
        int n = s.size();
        int max_len = 1;
        int start = 0;
        int dp[n][n] = {0};
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
            for (int j = 0; j < i; j++) {
                dp[j][i] = (s[i] == s[j] && (i-j < 2 || dp[j+1][i-1]));
                if (dp[j][i] && i-j+1 > max_len) {
                    max_len = i-j+1;
                    start = j;
                }
            }
        }
        std::cout << max_len << " " << start << "\n";
        return s.substr(start, max_len);
    }
};

int main()
{
    Solution solu;
    string s = "cbabe";
    string res = solu.longestPalindrome2(s);
    std::cout << res << "\n";
    return 0;
}
