# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        self.result = []
        self.temp = []
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node is None:
            return

        self.temp.append(str(node.val))
        if node.left is None and node.right is None:
            self.result.append("->".join(self.temp))
            # self.temp.pop()
            # return

        self.dfs(node.left)
        self.dfs(node.right)
        self.temp.pop()


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    # n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    # n2.left = n4
    n2.right = n5

    s = Solution()
    res = s.binaryTreePaths(n1)
    print(res)
