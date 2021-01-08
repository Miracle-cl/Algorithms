#include <iostream>
#include <vector>
#include <queue>
// #include <unordered_set>
#include <unordered_map>
#include <algorithm>

using std::vector;
using std::queue;
// using std::unordered_set;
using std::unordered_map;
using std::pair;
using std::make_pair;
using std::string;


class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // disjoint set
        unordered_map<string, int> n2i;
        int nodes = 0;
        for (auto& x : equations) {
            if (n2i.count(x[0]) == 0)
                n2i[x[0]] = nodes++;
            if (n2i.count(x[1]) == 0)
                n2i[x[1]] = nodes++;
        }
        vector<int> parents (nodes, 0);
        vector<double> weights (nodes, 1.0);
        for (int i = 0; i < nodes; i++)
            parents[i] = i;
        for (int i = 0; i < values.size(); i++) {
            int u = n2i[equations[i][0]];
            int v = n2i[equations[i][1]];
            merge(u, v, values[i], parents, weights);
        }
        vector<double> ans;
        for (const auto& q : queries) {
            double res = -1.0;
            if (n2i.count(q[0]) > 0 && n2i.count(q[1]) > 0) {
                int u = n2i[q[0]], v = n2i[q[1]];
                int pu = find(u, parents, weights);
                int pv = find(v, parents, weights);
                if (pu == pv)
                    res = weights[u] / weights[v];
            }
            ans.emplace_back(res);
        }

        return ans;
    }

    int find(int x, vector<int>& parents, vector<double>& weights) {
        if (x != parents[x]) {
            int t = parents[x];
            parents[x] = find(parents[x], parents, weights);
            weights[x] *= weights[t];
        }
        return parents[x];
    }

    bool merge(int u, int v, double w, vector<int>& parents, vector<double>& weights) {
        int pu = find(u, parents, weights);
        int pv = find(v, parents, weights);
        if (pu == pv) return false;
        parents[pu] = pv;
        weights[pu] = w * weights[v] / weights[u];
        return true;
    }

    vector<double> calcEquation_1(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // bfs
        unordered_map<string, int> n2i;
        int nodes = 0;
        for (auto& x : equations) {
            if (n2i.count(x[0]) == 0)
                n2i[x[0]] = nodes++;
            if (n2i.count(x[1]) == 0)
                n2i[x[1]] = nodes++;
        }
        vector<vector<double>> adj(nodes, vector<double>(nodes, 0));
        int n = values.size();
        for (int i = 0; i < n; i++) {
            int u = n2i[equations[i][0]], v = n2i[equations[i][1]];
            double w = values[i];
            adj[u][v] = w;
            adj[v][u] = 1/ w;
        }

        vector<double> ans;
        for (int i = 0; i < queries.size(); i++) {
            double res = -1.0;
            if (n2i.count(queries[i][0]) > 0 && n2i.count(queries[i][1]) > 0) {
                int u = n2i[queries[i][0]], v = n2i[queries[i][1]];
                res = bfs(nodes, u, v, adj);
                // std::cout << u << ' ' << v << ' ' << res << '\n';
            }
            ans.emplace_back(res);
        }
        return ans;
    }

    double bfs(const int nodes, int beg, int end, vector<vector<double>>& adj) {
        vector<int> visited(nodes, 0);
        visited[beg] = 1;
        queue<pair<int, double>> q;
        q.emplace(make_pair(beg, 1.0));
        while (!q.empty()) {
            int u = q.front().first;
            double w = q.front().second;
            q.pop();
            if (u == end) {
                adj[beg][end] = w;
                return w;
            }
            if (adj[u][end] > 0) {
                adj[beg][end] = w * adj[u][end];
                return adj[beg][end];
            }
            for (int cur = 0; cur < nodes; cur++) {
                if (visited[cur] == 0 && adj[u][cur] > 0) {
                    if (adj[beg][cur] == 0) adj[beg][cur] = w * adj[u][cur];
                    q.emplace(make_pair(cur, adj[beg][cur]));
                    visited[cur] = 1;
                }
            }
        }
        return -1.0;
    }
};

int main () 
{
    vector<vector<string>> equations {{"a","c"},{"b","e"},{"c","d"},{"e","d"}};
    vector<double> values {2.0,3.0,0.5,5.0};
    vector<vector<string>> queries {{"a","b"}};

    Solution sol;
    vector<double> ans = sol.calcEquation_1(equations, values, queries);
    for (double x : ans)
        std::cout << x << '\n';
    // int n = 5;
    // double adj[n][n] {0};
    // for (int i = 0; i < n; i++) 
    //     std::fill_n(adj[i], n, 0);

    // vector<vector<double>> adj(n, vector<double>(n, 0));
    // for (int i = 0; i < 2; i++) 
    //     printf("%d : %d\n", i, adj[0][i]);
    // for (int i = 0; i < 2; i++) 
    //     printf("%d : %d\n", i, adj[1][i]);
    return 0;
}
