from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j]: number of combinations with first i coins and total values is j
        n = len(coins)
        dp = [[0] * (1+amount) for _ in range(1+n)]
        dp[0][0] = 1
        for i in range(1, 1+n):
            c = coins[i-1]
            dp[i][0] = 1
            for j in range(1, 1+amount):
                if j >= c:
                    dp[i][j] = dp[i-1][j] + dp[i][j-c]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]

    def change_1d(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (1+amount)
        dp[0] = 1
        for c in coins:
            # for j in range(1, 1+amount):
            #     if j >= c:
            #         dp[j] += dp[j-c]
            for j in range(c, 1+amount):
                dp[j] = dp[j] + dp[j-c]
        return dp[amount]



coins = [1,2,5]
amount = 5
ss = Solution()
r1 = ss.change(amount, coins)
r2 = ss.change_1d(amount, coins)
print(r1, r2)