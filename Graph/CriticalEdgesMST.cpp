#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using std::vector;


class UnionFind {
private:
    vector<int> roots;
    vector<int> ranks;
public:
    explicit UnionFind(int n) : roots(n), ranks(n) {
        std::iota(roots.begin(), roots.end(), 0);
    }

    int find(int x) {
        return x == roots[x] ? x : roots[x] = find(roots[x]);
    }

    bool merge(int u, int v) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) return false;
        if (ranks[ru] == ranks[rv]) {
            roots[ru] = rv;
            ranks[rv]++;
        }
        else if (ranks[ru] < ranks[rv]) {
            roots[ru] = rv;
        }
        else {
            roots[rv] = ru;
        }
        return true;
    }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        const int n_e = edges.size();
        for (int i = 0; i < n_e; i++)
            edges[i].emplace_back(i);
        std::sort(edges.begin(), edges.end(), [](const auto& e1, const auto& e2) {
            return e1[2] < e2[2];
        });

        auto MST = [&](int ex=-1, int in=-1) -> int {
            // ex: drop edge ex; in: keep edge in
            UnionFind uf(n);
            int cost = 0, e_cnt = 0;
            if (in > -1) {
                uf.merge(edges[in][0], edges[in][1]);
                cost += edges[in][2];
                e_cnt++;
            }
            for (int i = 0; i < n_e; i++) {
                if (i == ex || i == in) continue;
                if (uf.merge(edges[i][0], edges[i][1])) {
                    cost += edges[i][2];
                    e_cnt++;
                }
                if (e_cnt == n-1) break;
            }
            return e_cnt == n-1 ? cost : INT32_MAX;
        };

        const int min_cost = MST();
        vector<int> cs, pcs;
        for (int i = 0; i < n_e; i++) {
            if (MST(i, -1) > min_cost) {
                cs.emplace_back(edges[i][3]);
            }
            else if (MST(-1, i) == min_cost) {
                pcs.emplace_back(edges[i][3]);
            }
        }
        return {cs, pcs};
    }
};


int main()
{
    int n = 6;
    vector<vector<int>> edges{{0,1,1},{1,2,1},{0,2,1},{2,3,4},{3,4,2},{3,5,2},{4,5,2}};
    Solution sol;
    vector<vector<int>> res = sol.findCriticalAndPseudoCriticalEdges(n, edges);
    return 0;
}

// n=4
// edges={{0,1,1},{0,3,1},{0,2,1},{1,2,1},{1,3,1},{2,3,1}}
// n=4
// edges = {{0,1,1},{1,2,1},{2,3,1},{0,3,1}}
// n=5
// edges={{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}}