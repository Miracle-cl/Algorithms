from typing import List

# houses = [0,0,0,0,0]
# cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
# m = 5
# n = 2
# target = 3

# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         return


# solu = Solution()
# res = solu.minCost(houses, cost, m, n, target)
# # arr = [1, 2, 3]
# # res = all(i > 2 for i in arr)
# print(res)


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         dp = [0] * (1+amount)
#         dp[0] = 1
#         for c in coins:
#             for i in range(c, 1+amount):
#                 dp[i] += dp[i-c]
#             print(dp)
#         return dp[amount]

# amount = 5
# coins = [1,2,5]
# solu = Solution()
# res = solu.change(amount, coins)
# print(res)


