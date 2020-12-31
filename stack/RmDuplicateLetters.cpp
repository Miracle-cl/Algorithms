#include <iostream>
#include <string>

using std::string;

// stack, greedy

class Solution {
public:
    string removeDuplicateLetters(string s) {
        string stk;
        int freqs[26] {0};
        int used[26] {0};
        for (char ch : s)
            freqs[ch - 'a']++;

        for (char ch : s) {
            if (!used[ch - 'a']) {
                while (!stk.empty() && stk.back() >= ch && freqs[stk.back() - 'a'] > 0) {
                    used[stk.back() - 'a'] = 0;
                    stk.pop_back();
                }
                stk.push_back(ch);
                used[ch - 'a'] = 1;
            }
            freqs[ch - 'a']--;
        }
        return stk;
    }
};

int main () 
{
    string s("ecbacba");
    Solution sol;
    string ans = sol.removeDuplicateLetters(s);
    std::cout << ans << '\n';
    return 0;
}