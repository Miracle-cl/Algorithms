from typing import List
from collections import deque
import heapq 


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # priority queue / BST: O(nlogn)
        q = []
        x, y = points[0]
        heapq.heappush(q, (x - y, x))
        ans = float('-inf')

        for j in range(1, len(points)):
            xj, yj = points[j]
            while q and xj - q[0][1] > k:
                heapq.heappop(q)
            if q:
                ans = max(ans, xj + yj - q[0][0])
            heapq.heappush(q, (xj - yj, xj))

        return ans

    def findMaxValueOfEquation_1(self, points: List[List[int]], k: int) -> int:
        # monotonic queue : O(n)
        mono_q = deque()
        x, y = points[0]
        mono_q.append((y - x, x))
        ans = float('-inf')

        for j in range(1, len(points)):
            xj, yj = points[j]
            while mono_q and xj - mono_q[0][1] > k:
                mono_q.popleft()
            if mono_q:
                ans = max(ans, xj + yj + mono_q[0][0])
            # push Pj: (yj - xj, xj)
            pj = (yj - xj, xj)
            while mono_q and mono_q[-1][0] < pj[0]:
                mono_q.pop()
            mono_q.append(pj)
            
        return ans



# points = [[1,3],[2,0],[5,10],[6,-10]]
# k = 1
# [[0,0],[3,0],[9,2]]
# 3