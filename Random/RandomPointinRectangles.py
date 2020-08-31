from typing import List
import random
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.tol = 0
        self.prefix = []
        for rect in self.rects:
            self.tol += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.prefix.append(self.tol)

    def pick(self) -> List[int]:
        point_id = random.randint(1, self.tol)
        rect_id = bisect.bisect_left(self.prefix, point_id)

        x1, y1, x2, _ = self.rects[rect_id]
        if rect_id > 0:
            point_id -= self.prefix[rect_id-1] # point_id in i-th rect
        width = x2 - x1 + 1
        x = (point_id - 1) % width + x1
        y = (point_id - 1) // width + y1
        return [x, y]

    # =================================== right ===================================
    # def __init__(self, rects: List[List[int]]):
    #     self.rects = rects
    #     self.tol = 0
    #     self.prefix = [0]
    #     for rect in self.rects:
    #         self.tol += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
    #         self.prefix.append(self.tol)

    # def pick(self) -> List[int]:
    #     pid = random.randint(0, self.tol-1)
    #     l, r = 0, len(self.prefix)
    #     while l < r:
    #         mid = (l + r) // 2
    #         if self.prefix[mid] <= pid:
    #             l = mid+1
    #         else:
    #             r = mid
    #     rect_id = l - 1
    #     x1, y1, x2, y2 = self.rects[rect_id]
    #     npoints = self.prefix[rect_id+1] - self.prefix[rect_id]
    #     pid = random.randint(1, npoints)
    #     # print(rect_id, npoints)
    #     x = (pid-1) % (x2-x1+1) + x1
    #     y = (pid-1) // (x2-x1+1) + y1
    #     return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

rects = [[-2, -2, -1, -1], [1, 0, 3, 0]]

obj = Solution(rects)
for _ in range(5):
    param_1 = obj.pick()
    print(param_1)