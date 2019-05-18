#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using std::string;
using std::vector;
using std::unordered_set;

class Solution {
public:
    bool wordBreak1(string s, vector<string>& wordDict) {
        unordered_set<string> word_set(wordDict.begin(), wordDict.end());
        vector<int> dp(s.size() + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= s.size(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j] == 1 && word_set.count(s.substr(j, i - j)) > 0) {
                    dp[i] = 1;
                    break;
                }
            }
        }
        return dp[s.size()];
    }

    bool wordBreak2(string s, vector<string>& wordDict) {
        // 8ms 10.9MB faster and smaller
        unordered_set<string> word_set(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.size(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp[j] && word_set.find(s.substr(j, i - j)) != word_set.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }

    vector<string> wordBreakII(string s, vector<string>& wordDict) {
        int n = s.size();
        unordered_set<string> wordset(wordDict.begin(), wordDict.end());
        vector<bool> dp(n+1, false);
        vector<vector<bool>> prev(n+1, vector<bool>(n+1, false));
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = i-1; j >= 0; j--) {
                if (dp[j] && wordset.find(s.substr(j, i-j)) != wordset.end()) {
                    dp[i] = true;
                    prev[j][i] = true;
                }
            }
        }
        vector<string> result;
        if (dp[n]) {
            vector<string> path;
            gen_path(s, prev, 0, path, result);
        }
        return result;
    }

    void print_vector(const vector<string> & vb) {
        for (auto x : vb)
            std::cout << x << "\n";
    }

private:
    void gen_path(const string & s, vector<vector<bool>> & prev, int curr, vector<string> & path,  vector<string> & result) {
        if (curr == s.size()) {
            string temp;
            for (auto sx: path)
                temp += sx + " ";
            temp.erase(temp.end() - 1); // delete lase space
            result.push_back(temp);
        }
        for (int i = curr + 1; i <= s.size(); i++) {
            if (prev[curr][i]) {
                path.push_back(s.substr(curr, i-curr));
                gen_path(s, prev, i, path, result);
                path.pop_back();
            }
        }
    }

};

// s = "pineapplepenapple"
// wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
// s = "catsanddog"
// wordDict = ["cat", "cats", "and", "sand", "dog"]

int main()
{
    // string s ("catsanddogs");
    // vector<string> vs {"cat", "cats", "and", "sand", "dog"};
    string s ("pineapplepenapple");
    vector<string> vs {"apple", "pen", "applepen", "pine", "pineapple"};
    Solution solu;
    vector<string> res = solu.wordBreakII(s, vs);
    solu.print_vector(res);
    // std::cout << s + " " + s1 << "\n";
    return 0;
}
