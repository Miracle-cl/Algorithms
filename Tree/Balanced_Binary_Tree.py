# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def height(self, node):
        if node:
            left_h = self.height(node.left)
            right_h = self.height(node.right)
            return 1 + max(left_h, right_h)
        else:
            return 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (not root):
            return True
        while (root.left or root.right):
            lh = self.height(root.left)
            rh = self.height(root.right)
            if abs(lh - rh) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        return True
