# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 100ms, 23.2MB
        _mem = {}
        
        def helper(root):
            if not root:
                return 0
            
            if root in _mem:
                return _mem[root]

            val = root.val
            if root.left:
                val = max(0, helper(root.left)) + root.val
            if root.right:
                val = max(val, root.val+helper(root.right))        

            _mem[root] = val
            return val
        
        
        q = [root]
        res = float('-inf')
        while q:
            node = q.pop()
            val = node.val
            if node.left:
                q.append(node.left)
                val = max(val, val + helper(node.left))
            if node.right:
                q.append(node.right)
                val = max(val, val + helper(node.right))
            res = max(res, val)
        return res

    def maxPathSum1(self, root: TreeNode) -> int:
        # 84ms, 20.5MB
        self.res = float('-inf')
        self.max_node_val(root)
        return self.res
        
    def max_node_val(self, root: TreeNode):
        if not root:
            return 0
        val = root.val
        left = self.max_node_val(root.left)
        right = self.max_node_val(root.right)
        max_nv = max(left, right, 0) + val
        self.res = max(self.res, max_nv, val+left+right)
        return max_nv