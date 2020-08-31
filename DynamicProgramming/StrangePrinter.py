class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        if n == 2:
            return 1 if s[0]==s[1] else 2
        dp = [[float('inf')] * n for _ in range(n)]
        # update dp[i][i]
        for i in range(n):
            dp[i][i] = 1
        # update dp[i][i+1]
        for i in range(n-1):
            dp[i][i+1] = 1 if s[i]==s[i+1] else 2
        # update dp[i][j] where i > j
        for i in range(1, n):
            for j in range(i):
                dp[i][j] = 0
        # update others
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = min(dp[i][j], dp[i][i] + dp[i+1][j]) # k = i
                for k in range(i+1, j+1):
                    second = 0 if k + 1 >= n else dp[k+1][j]
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k-1]+second)
                    # else:
                    #     dp[i][j] = min(dp[i][j], dp[i][k]+second)
        # print(dp)
        return dp[0][n-1]

    def strangePrinter_1(self, s: str) -> int:
        # memoization (faster)  
        memo = {}
        def dp(i, j):
            if i > j: 
                return 0
            if (i, j) not in memo:
                # if [i+1, j] no same as s[i] then i need to be print separately
                ans = dp(i+1, j) + 1 # k = i
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s) - 1)


ss = Solution()
s = "tbgtgb"
# res = ss.strangePrinter_1(s)
res = ss.strangePrinter(s)
print(res)