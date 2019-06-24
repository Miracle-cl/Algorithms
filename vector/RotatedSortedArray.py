from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]:
                if nums[l] <= target and nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[r-1] >= target and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
        return -1


nums = [4,5,6,7,0,1,2]
nums = [0,1,2,4,5,6,7]
nums = [1,2,4,5,6,7,0]
s = Solution()
res = s.search(nums, 7)
print(res)
