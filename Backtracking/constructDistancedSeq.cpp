#include <iostream>
#include <vector>


using std::vector;


class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        int lens = 2 * n - 1;
        vector<int> results(lens, 0);
        vector<bool> used(1+n, false);
        backtrack(0, n, lens, results, used);
        return results;
    }

    bool backtrack(int i, const int n, const int lens, vector<int>& results, vector<bool>& used) {
        if (i == lens) return true;
        if (results[i] > 0) return backtrack(i+1, n, lens, results, used);
        for (int k = n; k > 0; k--) {
            if (used[k]) continue;
            if (k > 1 && (i+k >= lens || results[i+k] > 0)) continue;
            results[i] = k;
            if (k > 1) results[i+k] = k;
            used[k] = true;
            if (not backtrack(i+1, n, lens, results, used)) {
                results[i] = 0;
                if (k > 1) results[i+k] = 0;
                used[k] = false;
            }
        }
        return results[i] > 0;
    }
};


int main () 
{
    int n = 10;

    Solution sol;
    vector<int> ans = sol.constructDistancedSequence(n);
    // vector<double> ans = sol.calcEquation_1(equations, values, queries);
    for (int x : ans)
        std::cout << x << ' ';
    std::cout << '\n';
    return 0;
}
