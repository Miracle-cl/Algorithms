from typing import List
# from pprint import pprint


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mode = 10 ** 9 + 7
        mem = {}

        def dfs(i, fuel):
            if fuel < 0:
                return 0
            if abs(locations[i]-locations[finish]) > fuel:
                return 0
            if (i, fuel) in mem:
                return mem[i, fuel]
            ans = 1 if i == finish else 0
            for j in range(n):
                if j == i:
                    continue
                # if j == finish:
                #     ans += 1
                ans += dfs(j, fuel - abs(locations[i]-locations[j]))
            mem[i, fuel] = ans % mode
            return ans

        res = dfs(start, fuel)
        # pprint(mem)
        return res  % mode


locations = [2,3,6,8,4]
start, finish, fuel = 1, 3, 5

# locations = [2,1,5]
# start, finish, fuel = 0,0,3
ss = Solution()
res = ss.countRoutes(locations, start, finish, fuel)
print(res)