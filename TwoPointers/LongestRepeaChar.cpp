#include <iostream>

using std::string;


class Solution {
public:
    int characterReplacement(string s, int k) {
        if (s.empty()) return 0;
        int n = s.length();
        int cnt[26] {0};
        int l = 0, r = 0;
        for (int more = 0; r < n; r++) {
            cnt[s[r] - 'A']++;
            more = std::max(more, cnt[s[r] - 'A']);
            if (r - l + 1 - more > k) {
                cnt[s[l] - 'A']--;
                l++;
            }
        }
        return r - l;
    }
};


int main () 
{
    string s ("AABABAB");
    int k = 3;
    Solution sol;
    int res = sol.characterReplacement(s, k);
    std::cout << res << '\n';

    return 0;
}