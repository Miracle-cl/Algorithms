from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        # dp[k][i]: min distance of k+1 mailbox in first i houses
        # cost[i][j]: min distance from house i to j with a mailbox
        _cost = {}
        def cost(i, j):
            if (i, j) in _cost:
                return _cost[(i, j)]
            res = 0
            l, r = i, j
            while l < r:
                res += houses[r] - houses[l]
                l += 1
                r -= 1
            _cost[(i, j)] = res
            return res

        dp = [[0] * n for _ in range(k)]
        for j in range(1, n):
            dp[0][j] = cost(0, j)

        for g in range(1, k):
            for i in range(g+1, n):
                dp[g][i] = min(dp[g-1][j] + cost(j+1, i) for j in range(0, i))

        # print(dp)
        # print(_cost)
        return dp[k-1][n-1]


houses = [1,4,8,10,20]
k = 3

ss = Solution()
res = ss.minDistance(houses, k)
print(res)