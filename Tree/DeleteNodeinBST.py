# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        print(root.val, end=', ')
        self.inorder(root.right)

    def insert_node(self, node, key):
        if not node:
            return TreeNode(key)
        if node.val < key:
            node.right = self.insert_node(node.right, key)
        elif node.val > key:
            node.left = self.insert_node(node.left, key)
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # root.val == key
            if not root.left:
                tmp = root.right
                # root = None
                return tmp
            if not root.right:
                tmp = root.left
                # root = None
                return tmp
            # both left and right is not None
            tmp = root.right
            while tmp and tmp.left:
                tmp = tmp.left
            root.val = tmp.val
            root.right = self.deleteNode(root.right, root.val)
        return root


if __name__ == '__main__':
    solu = Solution()
    root = None
    nums = [5,3,2,4,7,6,8]
    for n in nums:
        root = solu.insert_node(root, n)
    solu.inorder(root)
    print()
    solu.deleteNode(root, 5)
    solu.inorder(root)
    print()




