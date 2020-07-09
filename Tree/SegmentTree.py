from typing import List


class Node:
    # Segment Tree Node
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.sum = val
        self.left = left
        self.right = right
        
class SegmentTree:
    # def __init__(self):
    #     self.arr = arr
    
    def build_tree(self, arr: List[int], start: int, end: int) -> Node:
        if start == end:
            return Node(start, end, arr[start])
        mid = (start + end) // 2
        left = self.build_tree(arr, start, mid)
        right = self.build_tree(arr, mid+1, end)
        return Node(start, end, left.sum+right.sum, left, right)
    
    def update_tree(self, root: Node, i: int, val: int):
        if root.start == root.end == i:
            root.sum = val
            return
        mid = (root.start + root.end) // 2
        if i <= mid:
            self.update_tree(root.left, i, val)
        else:
            self.update_tree(root.right, i, val)
        root.sum = root.left.sum + root.right.sum
        
    def query_sum(self, root: Node, i: int, j: int) -> int:
        assert root, f'{i}, {j}'
        if root.start == i and root.end == j:
            return root.sum
        mid = (root.start + root.end) // 2
        if i > mid:
            return self.query_sum(root.right, i, j)
        if j <= mid:
            return self.query_sum(root.left, i, j)
        return self.query_sum(root.left, i, mid) + self.query_sum(root.right, mid+1, j)
    


# arr = [2,1,5,3,4]
# st = SegmentTree()
# n15 = st.build_tree(arr, 0, len(arr)-1)
# st.update_tree(n15, 4, 6)
# st.query_sum(n15, 1, 4)