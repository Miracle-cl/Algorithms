from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.dfs(root, sum)
        return self.res

    def dfs(self, node, sum):
        if (not node):
            return

        self.temp.append(node.val)
        if (node.left):
            self.dfs(node.left, sum - node.val)
            self.temp.pop()
        if (node.right):
            self.dfs(node.right, sum - node.val)
            self.temp.pop()
        if ((not node.left) and (not node.right) and (sum == node.val)):
            self.res.append(self.temp.copy())
            return
