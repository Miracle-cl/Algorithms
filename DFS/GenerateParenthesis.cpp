#include <iostream>
#include <vector>
#include <string>

using std::vector;
using std::string;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string temp;
        dfs(n, n, temp, res);
        return res;
    }

    void dfs1(int left, int right, string& temp, vector<string>& res) {
        if (left == 0 && right == 0) {
            res.push_back(temp);
            std::cout << temp << "\n";
            return;
        }
        if (left > 0) {
            temp.push_back('(');
            dfs(left-1, right, temp, res);
            temp.pop_back();
        }
        if (right > 0 && left < right) {
            temp.push_back(')');
            dfs(left, right-1, temp, res);
            temp.pop_back();
        }
    }
    // dfs1 == dfs2
    void dfs2(int left, int right, string& temp, vector<string>& res) {
        if (left > right)
            return;

        if (left == 0 && right == 0) {
            res.push_back(temp);
            std::cout << temp << "\n";
            return;
        }
        if (left > 0) {
            temp.push_back('(');
            dfs(left-1, right, temp, res);
            temp.pop_back();
        }
        if (right > 0) {
            temp.push_back(')');
            dfs(left, right-1, temp, res);
            temp.pop_back();
        }
    }
};

int main()
{
    int n = 3;
    Solution solu;
    vector<string> result = solu.generateParenthesis(n);
    return 0;
}
