class Solution {
public:
    int uniquePathsWithObstacles2(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size();
        int col = obstacleGrid[0].size();
        if (obstacleGrid[0][0] || obstacleGrid[row-1][col-1])
            return 0;
        if (row <= 1 || col <= 1)
            return 1;
        long dp[row][col]; // 1d vector is enough
        dp[0][0] = 1;
        for (int i = 1; i < col; i++) {
            // first row
            if (obstacleGrid[0][i] == 1 || dp[0][i-1] == 0)
                dp[0][i] = 0;
            else
                dp[0][i] = 1;
        }
        for (int i = 1; i < row; i++) {
            // first column
            if (obstacleGrid[i][0] == 1 || dp[i-1][0] == 0)
                dp[i][0] = 0;
            else
                dp[i][0] = 1;
        }
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (obstacleGrid[i][j] == 1)
                    dp[i][j] = 0;
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[row-1][col-1];
    }

    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size();
        int col = obstacleGrid[0].size();
        if (obstacleGrid[0][0] || obstacleGrid[row-1][col-1])
            return 0;
        int dp[col];
        for (int i = 0; i < row; i++) {
            dp[0] = (obstacleGrid[i][0] == 1) ? 0 : 1;
            for (int j = 1; j < col; j++) {
                dp[j] = (obstacleGrid[i][j] == 1) ? 0 : (dp[j-1] + dp[j]);
            }
        }
        return dp[col - 1];
    }
};
