from typing import List
from functools import lru_cache

class Solution:
    ## recursion with memory
    def canPartition(self, nums: List[int]) -> bool:
        sv = sum(nums)
        if sv % 2 == 1:
            return False
        tag = sv // 2
        # nums.sort()
        @lru_cache(maxsize=64)
        def helper(i, tag):
            if i < 0 or tag < 0:
                return False
            if tag == 0:
                return True
            return helper(i-1, tag-nums[i-1]) or helper(i-1, tag)

        return helper(len(nums)-1, tag-nums[-1]) or helper(len(nums)-1, tag)

    def canPartition0(self, nums: List[int]) -> bool:
        sv = sum(nums)
        if sv % 2 == 1:
            return False
        tag = sv // 2
        _mem = {}

        def helper(i, tag):
            if i < 0 or tag < 0:
                return False
            if tag == 0:
                return True
            if (i, tag) in _mem:
                return _mem[(i, tag)]
            _mem[(i, tag)] = helper(i-1, tag-nums[i-1]) or helper(i-1, tag)
            return _mem[(i, tag)]

        return helper(len(nums)-1, tag-nums[-1]) or helper(len(nums)-1, tag)

    ## dynamic programming
    def canPartition1(self, nums: List[int]) -> bool:
        sv = sum(nums)
        if sv % 2 == 1:
            return False
        tag = sv // 2
        dp = [0] * (sv + 1)
        dp[0] = 1
        for n in nums:
            for di in range(sv, -1, -1):
                if dp[di]:
                    dp[di+n] = 1
            if dp[tag]:
                return True
        return False

    def canPartition2(self, nums: List[int]) -> bool:
        sv = sum(nums)
        if sv % 2 == 1:
            return False
        tag = sv // 2
        sum_set = set([0])
        for n in nums:
            tmp = set()
            for x in sum_set:
                tmp.add(x + n)
            sum_set |= tmp
            if tag in sum_set:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    solu = Solution()
    res = solu.canPartition(nums)
    print(res)
