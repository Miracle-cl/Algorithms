from typing import List

class Solution:
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        _mem = {}
        size = len(cost)
        cost.append(0)
        
        def helper(i):
            if i < 0:
                return 0
            if i <= 1:
                return cost[i]
            if i in _mem:
                return _mem[i]
            _mem[i] = min(helper(i-1), helper(i-2))  + cost[i]
            return _mem[i]
        
        return helper(size)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        prev, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev, cur = cur, min(prev, cur) + cost[i]
        return cur


if __name__ == '__main__':
    solu = Solution()
    # cost = [0,0,0,0]
    # cost = [10,15,20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = solu.minCostClimbingStairs(cost)
    print(res)
