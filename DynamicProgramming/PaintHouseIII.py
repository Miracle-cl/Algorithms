from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf')] * n for _ in range(1+m)] for _ in range(1+target)]

        for k in range(1+target):
            for i in range(k, 1+m):
                if i == 0 and k == 0:
                    for j in range(n):
                        dp[k][i][j] = 0
                elif k == 0:
                    continue
                else:
                    hi = i-1
                    cj = houses[hi] - 1
                    if cj >= 0: # painted
                        # min(dp[k-1][i-1][!cj], dp[k][i-1][cj])
                        dp[k][i][cj] = min(dp[k-int(c!=cj)][i-1][c] for c in range(n))
                    else: # not painted
                        for j in range(n):
                            dp[k][i][j] = min(dp[k-int(c != j)][i-1][c] for c in range(n)) + cost[i-1][j]

        res = min(dp[target][m])
        return -1 if res == float('inf') else res


# houses = [0,0,0,0,0]
houses = [0,2,1,2,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3
ss = Solution()
res = ss.minCost(houses, cost, m, n, target)
print(res)