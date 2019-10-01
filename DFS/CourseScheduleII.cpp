#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses, vector<int> ());
        vector<int> visited(numCourses, 0);
        vector<int> path;
        for (auto p : prerequisites) {
            graph[p[1]].push_back(p[0]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, graph, visited, path))
                return {};
        }

        std::reverse(path.begin(), path.end());
        return path;
    }

    bool dfs(int i, vector<vector<int>>& graph, vector<int>& visited, vector<int>& path) {
        if (visited[i] == 1) return false;
        if (visited[i] == 2) return true;

        visited[i] = 1;
        for (auto nxt : graph[i]) {
            if (!dfs(nxt, graph, visited, path)) return false;
        }
        visited[i] = 2;
        path.push_back(i);
        return true;
    }
};

int main()
{
    int n = 4;
    vector<vector<int>> pairs {{1,0}, {2,0}, {3,1}, {3,2}};
    Solution s;
    vector<int> res = s.findOrder(n, pairs);
    for (auto n : res)
        std::cout << n << "\n";
    return 0;
}
