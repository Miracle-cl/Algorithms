from typing import List
from collections import deque
import heapq


class Solution:
    def maxResult_0(self, nums: List[int], k: int) -> int:
        # priority queue : O(nlogn)
        q = [(-nums[0], 0)]
        n = len(nums)
        ans = -nums[0]
        for i in range(1, n):
            while q and i - q[0][1] > k:
                heapq.heappop(q)
            ans = q[0][0] - nums[i]
            heapq.heappush(q, (ans, i))
            # print(q)    
        return -ans

    def maxResult(self, nums: List[int], k: int) -> int:
        # monotonic queue : O(n)
        q = deque([(nums[0], 0)])
        ans = nums[0]
        n = len(nums)
        for i in range(1, n):
            
            while q and (i - q[0][1] > k):
                q.popleft()
            ans = q[0][0] + nums[i]
            while q and ans >= q[-1][0]:
                q.pop()
            q.append((ans, i))
            
        return ans


if __name__ == '__main__':
    # nums = [1,-5,-20,4,-1,3,-6,-3]
    # k = 2

    # nums = [10,-5,-2,4,0,3]
    # k = 3

    nums = [1,-1,-2,4,-7,3]
    k = 2
    res = Solution().maxResult(nums, k)
    print(res)