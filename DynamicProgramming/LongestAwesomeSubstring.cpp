#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    int longestAwesome(string s) {
        constexpr int kinf = 1e9;
        vector<int> idx(1024, kinf);
        idx[0] = -1;
        int mask = 0;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            mask ^= 1 << (s[i] - '0');
            ans = std::max(ans, i - idx[mask]);
            for (int j = 0; j < 10; j++) {
                ans = std::max(i - idx[mask ^ (1 << j)], ans);
            }
            idx[mask] = std::min(i, idx[mask]);
        }
        return ans;
    }
};


int main()
{
    string s ("3242415");
    Solution ss;
    int res = ss.longestAwesome(s);
    std::cout << res << std::endl;
    return 0;
}