import bisect
# import heapq
from typing import List

class Node:
    # Segment Tree Node
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.sum = val
        self.left = left
        self.right = right
        
class Solution:
    def build(self, start, end):
        if start == end:
            return Node(start, end, 0)
        mid = (start + end) // 2
        left = self.build(start, mid)
        right = self.build(mid+1, end)
        return Node(start, end, 0, left=left, right=right)
        
    def count(self, root, start, end):
        assert root, f'{start}, {end}'
        if root.start == start and root.end == end:
            return root.sum
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self.count(root.left, start, end)
        if start > mid:
            return self.count(root.right, start, end)
        return self.count(root.left, start, mid) + self.count(root.right, mid+1, end)
    
    def insert(self, root, idx, val):
        assert root, f'{idx}, {val}'
        if root.start == root.end == idx:
            root.sum += val
            return
        mid = (root.start + root.end) // 2
        root.sum += val
        if idx <= mid:
            self.insert(root.left, idx, val)
        else:
            self.insert(root.right, idx, val)
        return 
    
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # prefix sum
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
            
        # descretization
        # si >= sj
        # lower <= (si - sj) <= upper
        # (si - upper) <= sj <= (si - lower)
        sum_set = set()
        for si in preSum:
            sum_set.add(si)
            sum_set.add(si-upper)
            sum_set.add(si-lower)
            
        sum_sorts = sorted(sum_set)
        # print(sum_sorts)
        ranks = {si: i for i, si in enumerate(sum_sorts)}
        
        root = self.build(0, len(ranks)-1)
        ans = 0
        for si in preSum:
            ans += self.count(root, ranks[si-upper], ranks[si-lower])
            self.insert(root, ranks[si], 1)
        return ans

# method with STL
# class Solution:
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         sum_ = [0]
#         prefix_ = 0
#         ans = 0
#         for num in nums:
#             prefix_ += num
#             ans += bisect.bisect_right(sum_, prefix_-lower) - bisect.bisect_left(sum_, prefix_-upper)
#             bisect.insort_left(sum_, prefix_)
#         return ans



if __name__ == '__main__':
    nums = [-1,2,-4,2,5,7,1,0]
    lower = -2
    upper = 2

    # nums = [0,-3,-3,1,1,2]
    # lower = 3
    # upper = 5


    # nums = [-3,1,2,-2,2,-1]
    # lower = -3
    # upper = -1
    # s_big - s_small : [lower, upper]
    # s_small : [s_big-upper, s_big-lower]

    ax = Solution()
    res = ax.countRangeSum(nums, lower, upper)
    print(res)