from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        maxv = nums[0]
        minv = nums[0]
        for i in range(1, len(nums)):
            _maxv, _minv = maxv*nums[i], minv*nums[i]
            maxv = max(_maxv, _minv, nums[i])
            minv = min(_maxv, _minv, nums[i])
            res = max(res, maxv)
        return res


if __name__ == '__main__':
    solu = Solution()
    # nums = [1,17,5,10,13,15,10,5,16,8]
    # nums = [1,2,3,4,5]
    nums = [2,3,-2,0,-4,3]
    res = solu.maxProduct(nums)
    print(res)