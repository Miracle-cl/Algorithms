from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count(target):
            cnt = 0
            j = 1
            for i in range(n-1):
                while j < n and nums[j]-nums[i] <= target:
                    j += 1
                cnt += j - i - 1
            return cnt
            
        l, r = 0, nums[-1]-nums[0]
        while l < r:
            mid = (l + r) // 2
            cnt = count(mid)
            if cnt < k:
                l = mid+1
            else:
                r = mid
        return l


# nums = [1,3,1,5,8]
# k = 5 # 3