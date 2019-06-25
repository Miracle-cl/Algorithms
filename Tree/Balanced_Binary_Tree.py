# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        lh = self.cal_height(root.left)
        rh = self.cal_height(root.right)
        if abs(lh - rh) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def cal_height(self, node):
        if node is None:
            return 0
        lh = self.cal_height(node.left)
        rh = self.cal_height(node.right)
        return 1 + max(lh, rh)
