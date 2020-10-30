#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

using std::string;
using std::vector;
using std::queue;
using std::unordered_map;
using std::unordered_set;


class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        unordered_set<string> visited;
        queue<string> q;
        q.emplace(s);
        visited.emplace(s);
        string ans = s;
        string cur, s_add, s_rot;
        int n = s.size();
        while (!q.empty()) {
            cur = q.front();
            ans = std::min(ans, cur);
            q.pop();
            // add
            s_add = cur;
            for (int i = 1; i < n; i += 2)
                s_add[i] = (s_add[i] - '0' + a) % 10 + '0';
            if (visited.count(s_add) == 0) {
                visited.emplace(s_add);
                q.emplace(s_add);
            }
            // rotate
            s_rot = cur.substr(n - b) + cur.substr(0, n - b);
            if (visited.count(s_rot) == 0) {
                visited.emplace(s_rot);
                q.emplace(s_rot);
            }
        }
        return ans;
    }
};


int main()
{
    Solution solu;
    string s("5525");
    string ans = solu.findLexSmallestString(s, 9, 2);
    std::cout << ans << '\n';
    return 0;
}