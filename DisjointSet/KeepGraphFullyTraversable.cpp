#include <iostream>
#include <vector>
#include <numeric>

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
        return x == roots[x] ? roots[x] : roots[x] = find(roots[x]);
    }

    bool merge(int u, int v) {
        int ru = find(u);
        int rv = find(v);
        if (ru == rv) return false;
        if (ranks[ru] < ranks[rv]) {
            roots[ru] = rv;
        }
        else if (ranks[ru] > ranks[rv]) {
            roots[rv] = ru;
        }
        else {
            roots[ru] = rv;
            ranks[rv]++;
        }
        return true;
    }
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        UnionFind ufa(1+n), ufb(1+n);
        int an = 0, bn = 0, ans = edges.size();
        for (auto& e : edges) {
            if (e[0] == 3) {
                if (ufa.merge(e[1], e[2])) {
                    an++, bn++, ans--;
                    ufb.merge(e[1], e[2]);
                }
            }
        }
        for (auto& e : edges) {
            if (e[0] == 1) {
                if (ufa.merge(e[1], e[2])) {
                    an++, ans--;
                }
            }
        }
        if (an < n-1) return -1;
        for (auto& e : edges) {
            if (e[0] == 2) {
                if (ufb.merge(e[1], e[2])) {
                    bn++, ans--;
                }
            }
        }
        if (bn < n-1) return -1;
        return ans;
    }
};


int main () 
{
    int n = 4;
    vector<vector<int>> edges {{3,1,2},{3,2,3},{1,1,3},{1,2,4},{1,1,2},{2,3,4}};
    Solution sol;
    int ans = sol.maxNumEdgesToRemove(n, edges);
    std::cout << ans << '\n';

    return 0;
}
