# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans += abs(left) + abs(right)
            return root.val + left + right - 1
        dfs(root)
        return ans

    # def distributeCoins(self, root: TreeNode) -> int:
    #     self.ans = 0
    #     def dfs(root):
    #         if not root:
    #             return 0
    #         left = dfs(root.left)
    #         right = dfs(root.right)
    #         self.ans += abs(left) + abs(right)
    #         return root.val + left + right - 1
    #     dfs(root)
    #     return self.ans