from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = j = 0
        zero = 0
        max_l = 0
        while i < len(nums) and j < len(nums):
            if zero == 0:
                if nums[j] == 0:
                    zero += 1
                j += 1
            elif zero == 1:
                if nums[j] == 0:
                    max_l = max(max_l, j - i)
                    zero += 1
                j += 1
            else: # zero == 2
                if nums[i] == 0:
                    zero -= 1
                i += 1
            # print([i, j, zero])

        if zero <= 1:
            max_l = max(max_l, j - i)
        return max_l - 1


# [1,1,0,1] - 3
# [0,1,1,1,0,1,1,0,1] - 5
# [1,1,1] - 2
# [1,1,0,0,1,1,1,0,1] - 4 
# [0,0,0] - 0