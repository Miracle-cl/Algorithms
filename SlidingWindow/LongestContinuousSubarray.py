from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        anchor = 0
        length = len(nums)
        max_q = deque()
        min_q = deque()
        ans = 1

        def push(i):
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()
            max_q.append(i)

            while min_q and nums[min_q[-1]] > nums[i]:
                min_q.pop()
            min_q.append(i)

        for i in range(length):
            push(i)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                if max_q[0] == anchor:
                    max_q.popleft()
                if min_q[0] == anchor:
                    min_q.popleft()
                anchor += 1
            ans = max(ans, i-anchor+1)
            # print(ans, max_q, min_q)
        return ans


# nums = [8,2,4,7], limit = 4 -> 2
# nums = [10,1,2,4,7,2], limit = 5 -> 4
# nums = [4,2,2,2,4,4,2,2], limit = 0 -> 3