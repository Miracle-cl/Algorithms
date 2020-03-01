from typing import List

class SegmentTreeNode:
    def __init__(self, start, end, sums, left=None, right=None):
        self.start = start
        self.end = end
        self.sums = sums
        self.left = left
        self.right = right


class NumArray:
    def __init__(self, nums: List[int]):
        if nums:
            self._root = self._build_tree(0, len(nums)-1, nums)
        else:
            self._root = None

    def update(self, i: int, val: int) -> None:
        self._update_tree(self._root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self._query_sum(self._root, i, j)

    def _build_tree(self, l, r, vals):
        if l == r:
            return SegmentTreeNode(l, r, vals[l])
        mid = (l+r) // 2
        left = self._build_tree(l, mid, vals)
        right = self._build_tree(mid+1, r, vals)
        return SegmentTreeNode(l, r, left.sums+right.sums, left, right)

    def _update_tree(self, root, idx, val):
        if not root:
            return
        if root.start == root.end == idx:
            root.sums = val
            return
        mid = (root.start + root.end) // 2
        if idx <= mid:
            self._update_tree(root.left, idx, val)
        else:
            self._update_tree(root.right, idx, val)
        root.sums = root.left.sums + root.right.sums

    def _query_sum(self, root, i, j):
        if not root:
            return 0
        if root.start == i and root.end == j:
            return root.sums
        mid = (root.start + root.end) // 2
        if j <= mid:
            return self._query_sum(root.left, i, j)
        if mid < i:
            return self._query_sum(root.right, i, j)
        return self._query_sum(root.left, i, mid) + self._query_sum(root.right, mid+1, j)


if __name__ == '__main__':
    # test1
    nums = [1, 3, 5]
    na9 = NumArray(nums)
    r1 = na9.sumRange(0, 2)
    na9.update(1, 2)
    r2 = na9.sumRange(0, 2)
    print(r1, r2)

    # test2
    nums = [2, 1, 5, 3, 4]
    na15 = NumArray(nums)
    r1 = na15.sumRange(3, 4)
    r2 = na15.sumRange(2, 2)
    # na15.update(2, 0)
    r3 = na15.sumRange(1, 3)
    print(r1, r2, r3)