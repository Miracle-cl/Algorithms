#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty())
            return 0;
        int r = grid.size(), c = grid[0].size();
        int max_area;
        int res = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 0)
                    continue;
                max_area = 0;
                max_area = dfs(grid, i, j, r, c, max_area);
                res = std::max(res, max_area);
            }
        }
        return res;
    }

    int dfs(vector<vector<int>>& grid, int i, int j, int r, int c, int max_area) {
        if (i < 0 || i >= r || j < 0 || j >= c || grid[i][j] == 0)
            return max_area;
        grid[i][j] = 0;
        max_area = 1 + dfs(grid, i-1, j, r, c, max_area)
                   + dfs(grid, i+1, j, r, c, max_area)
                   + dfs(grid, i, j-1, r, c, max_area)
                   + dfs(grid, i, j+1, r, c, max_area);
        return max_area;
    }
};

int main()
{
    vector<vector<int>> grid = {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                {0,1,1,0,1,0,0,0,0,0,0,0,0},
                                {0,1,0,0,1,1,0,0,1,0,1,0,0},
                                {0,1,0,0,1,1,0,0,1,1,1,0,0},
                                {0,0,0,0,0,0,0,0,0,0,1,0,0},
                                {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                {0,0,0,0,0,0,0,1,1,0,0,0,0}};

    Solution solu;
    int res = solu.maxAreaOfIsland(grid);
    std::cout << res << '\n';
    return 0;
}
