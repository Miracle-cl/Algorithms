from typing import List


class Node:
    # Segment Tree Node
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.sum = val
        self.left = left
        self.right = right


class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            self.root = None
        else:
            self.root = self.build(nums, 0, len(nums)-1)
        
    def build(self, nums: List[int], i:int, j:int) -> Node:
        if i == j:
            return Node(i, j, nums[i])
        mid = (i + j) // 2
        left = self.build(nums, i, mid)
        right = self.build(nums, mid+1, j)
        return Node(i, j, left.sum+right.sum, left, right)
        
    def update(self, i: int, val: int) -> None:
        def _update(node, i, val):
            if node.start == node.end == i:
                node.sum = val
                return
            mid = (node.start + node.end) // 2
            if i > mid:
                _update(node.right, i, val)
            else:
                _update(node.left, i, val)
            node.sum = node.left.sum + node.right.sum
        _update(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        def _query(node, i, j):
            if node.start == i and node.end == j:
                return node.sum
            mid = (node.start + node.end) // 2
            if i > mid:
                return _query(node.right, i, j)
            if j <= mid:
                return _query(node.left, i, j)
            return _query(node.left, i, mid) + _query(node.right, mid+1, j)
        return _query(self.root, i, j)
                


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)