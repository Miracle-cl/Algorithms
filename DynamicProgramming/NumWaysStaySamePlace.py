class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mode = 1000000007
        val_len = min((steps+3)//2, arrLen)
        # dp[i][j] : # of reach index j with i step
        dp = [[0] * val_len for i in range(1 + steps)]

        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        dp[0][0] = 1
        for i in range(1, 1+steps):
            for j in range(val_len):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                if j+1 < val_len:
                    dp[i][j] += dp[i-1][j+1]
                dp[i][j] %= mode
        return dp[steps][0]


if __name__ == '__main__':
    steps = 3
    arrLen = 2
    res = Solution().numWays(steps, arrLen)
    print(res)