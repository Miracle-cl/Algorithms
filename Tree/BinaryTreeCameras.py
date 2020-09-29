# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 0: node uncovered;
        # 1: node covered;
        # 2: node with camera
        cameras = 0
        def dfs(root):
            # return node state 
            nonlocal cameras
            if not root:
                return 1
            ls = dfs(root.left)
            rs = dfs(root.right)
            if ls == 0 or rs == 0:
                cameras += 1
                return 2
            if ls == 2 or rs == 2:
                return 1
            return 0

        if dfs(root) == 0:
            cameras += 1
        return cameras