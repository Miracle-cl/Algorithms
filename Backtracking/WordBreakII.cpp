#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using std::string;
using std::vector;
using std::unordered_map;
using std::unordered_set;

class Solution {
    unordered_map<int, vector<string>> mem;
    unordered_set<string> wordSet;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        wordSet = unordered_set(wordDict.begin(), wordDict.end());
        int n = s.size();
        mem[n] = {""};
        vector<string> res = backtrack(s, 0, n);
        return res;
    }

    vector<string> backtrack(const string& s, int idx, int n) {
        if (mem.count(idx) > 0) {
            return mem[idx];
        }
        vector<string> res;
        for (int i = idx+1; i <= n; i++) {
            string w = s.substr(idx, i - idx);
            if (wordSet.count(w) > 0) {
                vector<string> nxt = backtrack(s, i, n);
                for (string& sub_s : nxt) 
                    res.emplace_back(sub_s.empty() ? w : w + " " + sub_s);
            }
        }
        mem[idx] = res;
        return res;
    }
};

int main()
{
    Solution solu;
    string s("catsanddog");
    vector<string> wordDict {"cats", "cat", "and", "sand", "dog"};
    vector<string> ans = solu.wordBreak(s, wordDict);
    for (string& sub_s : ans)
        std::cout << sub_s << '\n';
    return 0;
}