from typing import List
from pprint import pprint
from collections import deque
import heapq, math
import bisect


locations = [2,3,6,8,4]
start, finish, fuel = 1, 3, 5

# locations = [2,1,5]
# start, finish, fuel = 0,0,3

# class Solution:
def countRoutes(locations: List[int], start: int, finish: int, fuel: int) -> int:
    n = len(locations)
    mem = {}

    def dfs(i, fuel):
        if fuel < 0:
            return 0
        if abs(locations[i]-locations[finish]) > fuel:
            return 0
        if (i, fuel) in mem:
            return mem[i, fuel]
        ans = 0
        for j in range(n):
            if j == i:
                continue
            if j == finish:
                ans += 1
            ans += dfs(j, fuel - abs(locations[i]-locations[j]))
        mem[i, fuel] = ans
        return ans

    res = dfs(start, fuel)
    pprint(mem)
    return res + (1 if start == finish else 0)


print([countRoutes(locations, start, finish, fuel)])

# arr = [1,2,3,3,3,4, 1,2,3]
# i = bisect.bisect_right(arr, 4, lo=0, hi=6)
# print(i)