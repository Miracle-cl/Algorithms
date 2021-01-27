#include <iostream>
#include <vector>
#include <algorithm>


using std::vector;



struct Edge {
    int len, x, y;
    Edge(int len, int x, int y) : len(len), x(x), y(y) {}
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        auto dist = [&](int x, int y) -> int {
            return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1]);
        };
        int n = points.size();
        vector<Edge> edges;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                edges.emplace_back(dist(i, j), i, j);
            }
        }
        std::sort(edges.begin(), edges.end(),
                  [](Edge a, Edge b) -> bool {return a.len < b.len;});
        int ans = 0, num = 1;
        vector<int> roots(n, 0);
        for (int i = 1; i < n; i++)
            roots[i] = i;

        for (auto& [len, x, y] : edges) {
            if (merge(x, y, roots)) {
                ans += len;
                num++;
                if (num == n) break;
            }
        }
        return ans;
    }

    int find(int x, vector<int>& roots) {
        if (x != roots[x]) 
            roots[x] = find(roots[x], roots);
        return roots[x];
    }

    bool merge(int u, int v, vector<int>& roots) {
        int ru = find(u, roots);
        int rv = find(v, roots);
        if (ru == rv) return false;
        roots[ru] = rv;
        return true;
    }
};



int main () 
{
    vector<vector<int>> points {{0,0},{2,2},{3,10},{5,2},{7,0}};

    Solution sol;
    int ans = sol.minCostConnectPoints(points);
    std::cout << ans << '\n';
    return 0;
}
