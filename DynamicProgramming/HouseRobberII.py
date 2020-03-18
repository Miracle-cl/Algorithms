from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        r1 = self.helper(nums[:-1])
        r2 = self.helper(nums[1:])
        return max(r1, r2)
        
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev, cur = cur, max(prev + nums[i], cur)
        return cur

if __name__ == '__main__':
    solu = Solution()
    # nums = [2]
    nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]
    res = solu.rob(nums)
    print(res)