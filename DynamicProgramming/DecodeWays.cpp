#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
    int numDecodings0(const std::string& s) {
        if (s.empty() || s[0] == '0')
            return 0;

        std::vector<int> dp(s.size() + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 1; i < s.size(); i++) {
            if ((s[i-1] == '1') || (s[i-1] == '2' && s[i] <= '6'))
                dp[i+1] += dp[i-1];
            if (s[i] != '0')
                dp[i+1] += dp[i];
        }
        return dp[s.size()];
    }

    int numDecodings(const std::string& s) {
        if (s.empty() || s[0] == '0')
            return 0;

        int prev = 1;
        int curr = 1;
        for (int i = 1; i < s.size(); i++) {
            int temp = 0;
            if ((s[i-1] == '1') || (s[i-1] == '2' && s[i] <= '6'))
                temp += prev;
            if (s[i] != '0')
                temp += curr;
            prev = curr;
            curr = temp;
        }
        return curr;
    }
};

int main()
{
    std::string s ("22");
    Solution solu;
    std::cout << solu.numDecodings(s) << "\n";
    return 0;
}
