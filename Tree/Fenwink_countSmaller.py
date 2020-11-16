from typing import List


class FenwinkTree:
    def __init__(self, n):
        self._sums = [0] * (1+n)
        self.n = n

    def update(self, i, delt):
        while i <= self.n:
            self._sums[i] += delt
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self._sums[i]
            i -= i & -i
        return ans


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        reverses = nums[::-1] # reversed nums
        sorts = sorted(set(nums)) # sorted unique nums
        ranks = {n: i for i, n in enumerate(sorts, 1)}

        res = []
        ft = FenwinkTree(len(sorts))
        for n in reverses:
            ft.update(ranks[n], 1)
            res.append(ft.query(ranks[n] - 1))
            print(ft._sums)
        return res[::-1]


# [5,2,6,1] -> [2,1,1,0]
nums = [7,1,3,2,9,2,1]
res = Solution().countSmaller(nums)
print(res)