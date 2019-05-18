#include <iostream>
#include <string>
#include <vector>

using std::vector;
using std::string;


class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> temp;
        dfs(0, s, temp, res);
        return res;
    }

    void dfs(int start, const string & s, vector<string> & temp, vector<vector<string>> & res) {
        if (start == s.size()) {
            res.push_back(temp);
            return;
        }
        else {
            for (int i = start; i < s.size(); i++) {
                if (isPalindrome(s, start, i)) {
                    // start = 0, i = 1 --------- substr size = 2
                    temp.push_back(s.substr(start, i+1-start));
                    dfs(i+1, s, temp, res);
                    temp.pop_back();
                }

            }
        }
    }

    bool isPalindrome(const string & s, int start, int end) {
        while (start < end) {
            if (s[start++] != s[end--])
                return false;
        }
        return true;
    }
    // bool isPalindrome(const string &s, int start, int end) {
    //     while (start < end && s[start] == s[end]) {
    //         ++start;
    //         --end;
    //     }
    //     return start >= end;
    // }

    void print_vector(vector<string> vs) {
        for (auto str : vs) {
            std::cout << str << "  ";
        }
        std::cout << "\n";
    }
};



class Solution2 {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        dfs(s, path, result, 0, 1);
        return result;
    }

    void dfs(string &s, vector<string>& path, vector<vector<string>> &result, size_t prev, size_t start) {
        if (start == s.size()) {
            if (isPalindrome(s, prev, start - 1)) {
                path.push_back(s.substr(prev, start - prev));
                // print_vector(path);
                result.push_back(path);
                path.pop_back();
            }
            return;
        }

        dfs(s, path, result, prev, start + 1);

        if (isPalindrome(s, prev, start - 1)) {
            path.push_back(s.substr(prev, start - prev));
            dfs(s, path, result, start, start + 1);
            path.pop_back();
        }
    }

    bool isPalindrome(const string &s, int start, int end) {
        while (start < end && s[start] == s[end]) {
            ++start;
            --end;
        }
        return start >= end;
    }

    void print_vector(vector<string> vs) {
        for (auto str : vs) {
            std::cout << str << "  ";
        }
        std::cout << "\n";
    }
};


int main()
{
    string str ("aab");
    Solution s;
    vector<vector<string>> result = s.partition(str);
    for (auto vs : result)
        s.print_vector(vs);
    return 0;
}

const int m = obstacleGrid.size();
const int n = obstacleGrid[0].size();
if (obstacleGrid[0][0] || obstacleGrid[m-1][n-1]) return 0;
vector<int> f(n, 0);
f[0] = obstacleGrid[0][0] ? 0 : 1;
for (int i = 0; i < m; i++) {
    f[0] = f[0] == 0 ? 0 : (obstacleGrid[i][0] ? 0 : 1);
    for (int j = 1; j < n; j++)
        f[j] = obstacleGrid[i][j] ? 0 : (f[j] + f[j - 1]);
}
return f[n - 1];
