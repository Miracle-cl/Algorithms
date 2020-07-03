from typing import List
from collections import deque


class Solution:
    """
    monotonic queue & dynamic programming
    """
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp[i]: max value to i with nums[i]
        # dp[i] = max(dp[i-k], dp[i-k+1] ... dp[i-1], 0) + nums[i]
        _win = deque(maxlen=k) # monotonic queue: store index of nums
        dp = [0] * len(nums)

        def push(i):
            if _win:
                dp[i] = max(dp[_win[0]] + nums[i], nums[i])
            else:
                dp[i] = nums[i]
            while _win and dp[_win[-1]] < dp[i]:
                _win.pop()
            _win.append(i)

        for i in range(len(nums)):
            if _win and i - _win[0] > k:
                _win.popleft()
            push(i)
        return max(dp)
        

# nums = [10,2,-10,5,20], k = 2 -> 37
# nums = [-1,-2,-3], k = 1
# nums = [10,-2,-10,-5,20], k = 2