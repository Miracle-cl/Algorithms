#include <iostream>
#include <string>
#include <vector>
#include <climits>

using std::string;
using std::vector;


class Solution {
public:
    vector<int> splitIntoFibonacci(string S) {
        vector<int> ans;
        int n = S.length();
        backtrack(ans, S, 0, n, 0, 0);
        return ans;
    }
    
    bool backtrack(vector<int>& ans, const string& s, int i, int n, long long sum, int pre) {
        // std::cout << pre << '\n';
        if (i == n)
            return ans.size() > 2;
        long long cur = 0;
        for (int j = i; j < n; j++) {
            if (s[i] == '0' && j > i)
                break;
            cur = cur * 10 + s[j] - '0';
            if (cur > INT32_MAX)
                break;
            if (ans.size() < 2 || cur == sum) {
                ans.emplace_back(cur);
                if (backtrack(ans, s, j+1, n, pre+cur, cur))
                    return true;
                ans.pop_back();
            }
            else if (cur > sum)
                break;
        }
        return false;
    }
};

int main()
{
    string s("123456579");
    Solution solu;
    vector<int> res = solu.splitIntoFibonacci(s);
    for (auto x: res)
        std::cout << x << '\n';
    return 0;
}
