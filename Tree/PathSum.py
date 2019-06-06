from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deserialize(arr):
    # level order
    if not arr:
        return None
    root = TreeNode(arr.pop(0))
    queue = [root]
    while queue:
        node = queue.pop(0)
        if arr:
            val = arr.pop(0)
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
        if arr:
            val = arr.pop(0)
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
    return root


class PathSumII:
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


class PathSumIII:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0
        self.preorder(root, sum)
        return self.cnt

    def preorder(self, node, sum):
        # traverse all node
        if node is None:
            return
        self.helper(node, sum)
        self.preorder(node.left, sum)
        self.preorder(node.right, sum)

    def helper(self, node, sum):
        # judge sum
        if node is None:
            return
        if node.val == sum:
            self.cnt += 1
        self.helper(node.left, sum-node.val)
        self.helper(node.right, sum-node.val)

if __name__ == "__main__":
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \    / \
    # 7    2  5   1

    ps2 = PathSumII()
    arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    # print(len(arr)) #13
    root2 = deserialize(arr)
    res2 = ps2.pathSum(root2, 22)
    print(res2)


    # ======================================================
    #       10
    #      /  \
    #     5   -3
    #    / \    \
    #   3   2   11
    #  / \   \
    # 3  -2   1

    arr3 = [10,5,-3,3,2,None,11,3,-2,None,1]
    root3 = deserialize(arr3)
    ps3 = PathSumIII()
    res3 = ps3.pathSum(root3, 8)
    print(res3)
