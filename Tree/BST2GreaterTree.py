# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def mid_traverse(self, node):
        if node == None:
            return
        self.mid_traverse(node.right)
        node.val += self.result
        self.result = node.val
        self.mid_traverse(node.left)

    def convertBST1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.mid_traverse(root)
        return root

    def convertBST2(self, root: TreeNode) -> TreeNode:
        stk = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            stk.append(node)
            inorder(node.right)

        add_value = 0
        inorder(root)
        while stk:
            top = stk.pop()
            add_value += top.val
            top.val = add_value
        return root

    def convertBST3(self, root: TreeNode) -> TreeNode:
        self.v = 0 # use [v] is OK
        def inorder(node):
            if node is None:
                return
            inorder(node.right)
            self.v += node.val
            node.val = self.v
            inorder(node.left)

        inorder(root)
        return root

def create_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    return root

if __name__ == "__main__":
    root = create_tree()
    s = Solution()
    result = s.convertBST1(root)
    print(">>result: ", result)
