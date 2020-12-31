#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <iterator>

using std::pair;
using std::string;
using std::vector;
using std::list;
using std::queue;
using std::deque;
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> mp;
        int n = s.length();
        size_t begin = 0, end = 0;
        for (char c : pattern) {
            if (begin > n) return false;
            end = s.find(' ', begin);
            if (end == string::npos) end = n;
            string w = s.substr(begin, end-begin);
            if (mp.count(c) > 0 && mp[c] != w) return false;
            mp[c] = w;
            begin = ++end;
        }
        if (begin <= n) return false;
        unordered_set<string> used;
        for (auto& x : mp) {
            if (used.count(x.second) > 0) return false;
            used.emplace(x.second);
        }
        return true;
    }

    bool wordPattern_0(string pattern, string s) {
        unordered_map<char, string> mp;
        int n = s.length();
        int begin = 0, end = 0;
        for (char c : pattern) {
            if (begin > n) return false;
            while (end < n && s[end] != ' ')
                end++;
            string w = s.substr(begin, end-begin);
            if (mp.count(c) > 0 && mp[c] != w)
                return false;
            mp[c] = w;
            begin = ++end;
        }
        if (begin <= n) return false;
        unordered_set<string> used;
        for (auto& x : mp) {
            if (used.count(x.second) > 0) return false;
            used.emplace(x.second);
        }
        return true;
    }
};

int main()
{
    Solution solu;
    string str("dog cat cat dog");
    bool res0 = solu.wordPattern("abba", str);
    bool res1 = solu.wordPattern("aa", "aa aa aa");
    bool res2 = solu.wordPattern("aaaa", "aa aa aa");
    bool res3 = solu.wordPattern("jquery", "jquery");

    std::cout << res0 << '\n';
    std::cout << res1 << '\n';
    std::cout << res2 << '\n';
    std::cout << res3 << '\n';
    return 0;

}