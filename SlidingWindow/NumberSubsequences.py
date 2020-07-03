from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mode = 10**9 + 7
        ans = 0
        length = len(nums)
        nums.sort()

        pow2 = [1] * (1 + len(nums))
        for i in range(len(nums)):
            pow2[i+1] = pow2[i] * 2 % mode

        for i, n in enumerate(nums):
            if n * 2 > target:
                break
            max_i = bisect.bisect_right(nums, target-n, lo=i, hi=length) - 1
            ans += pow2[max_i - i]
            ans %= mode
            # print(i, max_i)
        return ans

    def numSubseq_1(self, nums: List[int], target: int) -> int:
        mode = 10**9 + 7
        ans = 0
        length = len(nums)
        nums.sort()

        pow2 = [1] * (1 + len(nums))
        for i in range(len(nums)):
            pow2[i+1] = pow2[i] * 2 % mode

        def search(lo, hi, tgt):
            l, r = lo, hi
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= tgt:
                    l = mid + 1
                else:
                    r = mid
            return l-1 if nums[l] > tgt else l

        for i, n in enumerate(nums):
            if n * 2 > target:
                break
            max_i = search(lo=i, hi=length-1, tgt=target-n)
            ans += pow2[max_i - i]
            ans %= mode
            # print(i, max_i)
        return ans

    def numSubseq_2(self, nums: List[int], target: int) -> int:
        mode = 10**9 + 7
        ans = 0
        length = len(nums)
        nums.sort()

        pow2 = [1] * (1 + len(nums))
        for i in range(len(nums)):
            pow2[i+1] = pow2[i] * 2 % mode

        def search(lo, hi, tgt):
            l, r = lo, hi
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= tgt:
                    l = mid + 1
                else:
                    r = mid
            return l-1 if l >= length or nums[l] > tgt else l

        for i, n in enumerate(nums):
            if n * 2 > target:
                break
            max_i = search(lo=i, hi=length, tgt=target-n)
            ans += pow2[max_i - i]
            ans %= mode
            # print(i, max_i)
        return ans



nums = [3,5,6,7], target = 9
nums = [3,3,6,8], target = 10
nums = [2,3,3,4,6,7], target = 12
nums = [5,2,4,1,7,6,8], target = 16
[7,10,7,3,7,5,4]