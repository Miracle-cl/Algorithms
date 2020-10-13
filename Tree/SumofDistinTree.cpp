#include <iostream>
#include <vector>

using std::vector;


class Solution {
public:
    vector<int> sumOfDistancesInTree(int N, vector<vector<int>>& edges) {
        vector<int> cnt(N, 0);
        vector<int> res(N, 0);
        vector<vector<int>> g(N, vector<int>(0));
        for (auto e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        postorder(0, -1, cnt, res, g);
        preorder(0, -1, N, cnt, res, g);
        return res;
    }

    void postorder(int u, int pre, vector<int>& cnt, vector<int>& res, vector<vector<int>>& g) {
        for (int v : g[u]) {
            if (v == pre) continue;
            postorder(v, u, cnt, res, g);
            cnt[u] += cnt[v];
            res[u] += res[v] + cnt[v];
        }
        cnt[u]++;
        return;
    }

    void preorder(int u, int pre, const int N, const vector<int>& cnt, vector<int>& res, vector<vector<int>>& g) {
        for (int v : g[u]) {
            if (v == pre) continue;
            res[v] = res[u] + N - cnt[v] - cnt[v];
            preorder(v, u, N, cnt, res, g);
        }
        return;
    }
};


int main()
{
    int N = 6;
    vector<vector<int>> edges{{0,1},{0,2},{2,3},{2,4},{2,5}};
    Solution solu;
    vector<int> res = solu.sumOfDistancesInTree(N, edges);
    for (int x: res)
        std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}