# dp[n][0] : in n column fully filled
# dp[n][1] : in n column , first row is empty
# dp[n][2] : in n column , second row is empty
# dp[n][0] = dp[n-1][0] + dp[n-2][0] + dp[n-1][1] + dp[n-1][2]
# dp[n][1] = dp[n-2][0] + dp[n-1][2]
# dp[n][2] = dp[n-2][0] + dp[n-1][1]
# dp[n][1], dp[n][2] is symmetric, so keep 0, 1 is enough

class Solution:
    def numTilings(self, N: int) -> int:
        # dp[i][j]: in i column, loss j square
        mode = 10 ** 9 + 7
        dp = [[0, 0] for _ in range(max(1+N, 3))]
        dp[1][0] = 1
        dp[2][0] = 2
        dp[2][1] = 1
        if N < 3:
            return dp[N][0]
        for i in range(3, 1+N):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] * 2) % mode
            dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % mode # symmetric
        return dp[N][0]


ss = Solution()
ss.numTilings(4)