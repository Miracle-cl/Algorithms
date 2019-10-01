#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses, vector<int> ());
        // visited {0: unvisited, 1: visiting, 2: visited}
        vector<int> visited(numCourses, 0);
        for (auto p : prerequisites) {
            graph[p[1]].push_back(p[0]);
        }
        for (int i = 0; i < visited.size(); i++) {
            if (!dfs(i, graph, visited)) return false;
        }
        return true;
    }

    bool dfs(int start, vector<vector<int>>& graph, vector<int>& visited) {
        if (visited[start] == 1) return false;
        if (visited[start] == 2) return true;

        visited[start] = 1;
        for (auto end : graph[start]) {
            if (!dfs(end, graph, visited)) return false;
        }
        visited[start] = 2;
        return true;
    }
};

int main()
{
    Solution s;
    int n = 4;
    vector<vector<int>> p {{0,1}, {3,1}, {1,2}, {2,3}};
    bool res = s.canFinish(n, p);
    std::cout << res << "\n";
    return 0;
}
