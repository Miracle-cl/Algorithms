from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if len(arr) < 2:
            return -1
        prefix = self.min_length(arr, target)
        prefix = [float('inf')] + prefix[:-1] # befor i
        suffix = self.min_length(arr[::-1], target)
        suffix = suffix[::-1] # at and after i
        res = float('inf')
        for i in range(len(arr)):
            res = min(res, prefix[i] + suffix[i])
        return res if res < float('inf') else -1
    
    @staticmethod
    def min_length(arr: List[int], target: int) -> List[int]:
        # befor and at i
        presum = arr.copy()
        m = {0: -1, arr[0]: 0}
        prefix = [float('inf')] * len(arr)
        if arr[0] == target:
            prefix[0] = 1
        for i in range(1, len(arr)):
            presum[i] += presum[i-1]
            delt = presum[i] - target
            ml = min(prefix[i-1], i - m[delt]) if delt in m else prefix[i-1]
            prefix[i] = ml
            m[presum[i]] = i
        return prefix


# arr = [5,5,4,4,5]
arr = [3,2,2,4,3]
target = 3
ss = Solution()
res = ss.minSumOfLengths(arr, target)
print(res)