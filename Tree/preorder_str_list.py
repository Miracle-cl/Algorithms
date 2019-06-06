# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_str(node, res):
    if node is None:
        return ''
    l = preorder_str(node.left, res)
    r = preorder_str(node.right, res)
    return str(node.val) + l + r



def preorder_l1(node, res):
    if node is None:
        return []
    l = preorder_l1(node.left, res)
    r = preorder_l1(node.right, res)
    return [node.val] + l + r


def f(root):
    res = []
    def preorder(node):
        if node is None:
            return
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    r1 = preorder_str(root, '')
    r2 = preorder_l1(root, [])
    r3 = f(root)

    print(r1)
    print(r2)
    print(r3)
