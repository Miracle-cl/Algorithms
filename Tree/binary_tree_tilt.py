# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse(self, node):
        if (node is None):
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.tilt += abs(left - right)
        return left + right + node.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.traverse(root)
        return self.tilt

def create_tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    return root

if __name__ == "__main__":
    root = create_tree()
    s = Solution()
    result = s.findTilt(root)
    print(">>result: ", result)
