#include <iostream>
#include <vector>

using std::vector;


class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        int r = rowSum.size();
        int c = colSum.size();
        vector<vector<int>> ans(r, vector<int>(c, 0));
        int i = 0, j = 0;
        int x;
        while (i < r && j < c) {
            x = std::min(rowSum[i], colSum[j]);
            ans[i][j] = x;
            rowSum[i] -= x;
            colSum[j] -= x;
            if (rowSum[i] == 0) i++;
            if (colSum[j] == 0) j++;
        }
        return ans;
    }
};

int main()
{
    vector<int> rowSum{5,7,10};
    vector<int> colSum{4,6,4,8};
    Solution solu;
    vector<vector<int>> ans = solu.restoreMatrix(rowSum, colSum);
    for (auto c: ans) {
        for (int x : c) {
            std::cout << x << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}