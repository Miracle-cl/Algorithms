from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0:
            return r
        # else rm shortest subarray which sum % p == r
        # sum = prefix[y] - prefix[x] = py - px
        # let: py = n * p + y; px = n * p + x
        # so: x - y = r or r - p
        # so: y = x - r or r - r + p

        sum_loc = {}
        prefix = 0
        ans = float('inf')
        for i, n in enumerate(nums):
            prefix += n
            mode_x = prefix % p
            if mode_x >= r:
                mode_y = mode_x - r
            else:
                mode_y = mode_x - r + p
            
            if mode_y in sum_loc:
                ans = min(ans, i - sum_loc[mode_y])
            sum_loc[mode_x] = i

        return ans if ans < len(nums) else -1


nums = [5,1,3,4,2,6]
p = 11

# nums = [5,2,6,3]
# p = 9
