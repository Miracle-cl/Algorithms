from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        begin = 0
        c_neg = 0
        ans = 0

        def cal_max_len(l, r, c_neg):
            if c_neg % 2 == 0:
                return r - l
            i = l
            while i < r:
                if nums[i] > 0:
                    i += 1
                else:
                    break
            ans = r - i - 1
            j = r - 1
            while j >= l:
                if nums[j] > 0:
                    j -= 1
                else:
                    break
            ans = max(ans, j - l)
            return ans

        for i, n in enumerate(nums):
            if n == 0:
                ans = max(ans, cal_max_len(begin, i, c_neg))
                begin = i + 1
                c_neg = 0
            elif n < 0:
                c_neg += 1

        ans = max(ans, cal_max_len(begin, i+1, c_neg)) # final subarray
        return ans


nums = [1,-2,-3,-4,5,6,0,-1,-2,-3,-4,-5,-6]
ss = Solution()
res = ss.getMaxLen(nums)
print(res)