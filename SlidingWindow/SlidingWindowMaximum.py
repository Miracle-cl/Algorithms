from typing import List
from collections import deque
import heapq


class MonotonicQueue:
    def __init__(self):
        self.data = deque()
        
    def push(self, e):
        while self.data and self.data[-1] < e:
            self.data.pop()
        self.data.append(e)
        
    def pop(self):
        if self.data:
            self.data.popleft()
        
    def get_max(self):
        return self.data[0] if self.data else -1


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = MonotonicQueue()
        for i in range(k):
            mq.push(nums[i])
            # print(mq.data)

        ans = [mq.get_max()]
        for i in range(k, len(nums)):
            mq.push(nums[i])
            if mq.get_max() == nums[i-k]:
                mq.pop()
            # print(mq.data)
            ans.append(mq.get_max())
        return ans

    def maxSlidingWindow_simp(self, nums: List[int], k: int) -> List[int]:
        # use deque merge class MonotonicQueue in one function
        q = deque() # store index of nums
        
        def push(i):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        for i in range(k):
            push(i)
            
        ans = [nums[q[0]]]
        for i in range(k, len(nums)):
            push(i)
            if i - q[0] >= k:
                q.popleft()
            ans.append(nums[q[0]])
        return ans

    def maxSlidingWindow_bt(self, nums: List[int], k: int) -> List[int]:
        # binary tree
        h = []
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))
            
        ans = [-h[0][0]]
        visited = set()
        for i in range(k, len(nums)):
            visited.add(i-k)
            heapq.heappush(h, (-nums[i], i))
            while h and h[0][1] in visited:
                heapq.heappop(h)
            ans.append(-h[0][0])
        return ans


# nums = [1,3,-1,-3,5,3,6,7]
nums = [6,5,4,3,1,3,-1,-3,5,3,6,7]
k = 3
ss = Solution()
res1 = ss.maxSlidingWindow(nums, k)
print(res1)