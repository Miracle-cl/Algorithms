# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.diameter = 0

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            node_d = 1 + max(left, right)
            self.diameter = max(self.diameter, left+right)
            return node_d

        helper(root)
        return self.diameter

    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        if not root:
            return 0

        _height = {}

        def height(root):
            if not root:
                return 0
            if root in _height:
                return _height[root]
            _height[root] = 1 + max(height(root.left), height(root.right))
            return _height[root]

        height(root)
        q = [root]
        diameter = 0
        while q:
            node = q.pop()
            diameter = max(diameter, 
                           height(node.left) + height(node.right))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return diameter