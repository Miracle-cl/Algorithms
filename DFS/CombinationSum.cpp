#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;

// ============ a little slowere ================================================================================
// void dfs(int, int, vector<vector<int>>&, vector<int>&, const vector<int>&);
//
// vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
//     vector<vector<int>> res;
//     vector<int> temp;
//     std::sort(candidates.begin(), candidates.end());
//     dfs(0, target, res, temp, candidates);
//     return res;
// }
//
// void dfs(int start, int target, vector<vector<int>>& res, vector<int>& temp, const vector<int>& candidates) {
//     if (target == 0) {
//         res.push_back(temp);
//         for (auto i : temp)
//             std::cout << i << " ";
//         std::cout << "\n";
//         return;
//     }
//     if (target < 0) {
//         return;
//     }
//     for (int i = start; i < candidates.size(); i++) {
//         if (target >= candidates[i]) {
//             temp.push_back(candidates[i]);
//             dfs(i, target-candidates[i], res, temp, candidates);
//             temp.pop_back();
//             // target += candidates[i];
//         }
//     }
// }

class Solution1 {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> temp;
        std::sort(candidates.begin(), candidates.end());
        dfs(0, target, res, temp, candidates);
        return res;
    }

    void dfs(int start, int target, vector<vector<int>>& res, vector<int>& temp, const vector<int>& candidates) {
        if (target == 0) {
            res.push_back(temp);
            for (auto x : temp)
                std::cout << x << " ";
            std::cout << "\n";
            return;
        }
        if (target < 0) {
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (target < candidates[i])
                return; // faster
            temp.push_back(candidates[i]);
            dfs(i, target-candidates[i], res, temp, candidates);
            temp.pop_back();
            // target += candidates[i];
        }
    }
};

class Solution2 {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> temp;
        std::sort(candidates.begin(), candidates.end());
        dfs(0, target, res, temp, candidates);
        return res;
    }

    void dfs(int start, int target, vector<vector<int>>& res, vector<int>& temp, const vector<int>& candidates) {
        if (target == 0) {
            res.push_back(temp);
            for (auto x : temp)
                std::cout << x << " ";
            std::cout << "\n";
            return;
        }
        if (target < 0) {
            return;
        }
        int prev = -1;
        for (int i = start; i < candidates.size(); i++) {
            if (target < candidates[i])
                return; // faster
            if (candidates[i] == prev)
                continue;
            prev = candidates[i];
            temp.push_back(candidates[i]);
            dfs(i+1, target-candidates[i], res, temp, candidates);
            temp.pop_back();
            // target += candidates[i];
        }
    }
};

int main()
{
    // vector<int> candidates {2,3,6,7};
    // vector<int> candidates {2,3,5};
    vector<int> candidates {10,1,2,7,6,1,5};
    int target = 8;
    Solution2 solu;
    vector<vector<int>> res = solu.combinationSum2(candidates, target);
    return 0;
}
