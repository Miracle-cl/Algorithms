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




# nums = [1,2,4,8]
# dp = [0] * 4
# parent = [0] * 4
# res = []
# mx = mx_i = 0

# for i in range(3, -1, -1):
#     for j in range(i, 4):
#         if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
#             dp[i] = dp[j] + 1
#             parent[i] = j
#             if mx < dp[i]:
#                 mx = dp[i]
#                 mx_i = i

# print(dp)
# print(parent)
# for i in range(mx):
#     res.append(nums[mx_i])
#     mx_i = parent[mx_i]
# print(res)

# dp[0] = 1
# dp[i] = max(dp[k]) + 1 if nums[i] % nums[k] == 0 and 0<=k<i

nums = [1,2,4,6,8,10]
# nums = [3,4,7,8,10]
# nums = [1]
l = len(nums)
dp = [1] * l
parent = list(range(l))

mx_v = mx_i = 0
for i in range(1, l):
    for k in range(i):
        if nums[i] % nums[k]==0 and dp[k]+1>dp[i]:
            dp[i] = dp[k] + 1
            parent[i] = k
    if dp[i] > mx_v:
        mx_v = dp[i]
        mx_i = i

# print(dp)
# print(parent)
# print(mx_v, mx_i)

res = []
while mx_i != parent[mx_i]:
    res.append(nums[mx_i])
    mx_i = parent[mx_i]

res.append(nums[mx_i])



print(res)