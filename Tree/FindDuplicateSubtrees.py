import collections
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(nums: str) -> TreeNode:
    if not nums:
        return None
    nums = [None if n == '#' else int(n) for n in nums.split(',')]
    nums.reverse()
    root = TreeNode(nums.pop())
    q = collections.deque([root])
    while q:
        node = q.popleft()
        if nums:
            val = nums.pop()
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
        if nums:
            val = nums.pop()
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
    return root


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        series2node = collections.defaultdict(list)
        
        def serialize(root):
            if not root:
                return '#'
            series = ','.join([str(root.val), serialize(root.left), serialize(root.right)])
            series2node[series].append(root)
            return series
        
        serialize(root)
        print(list(series2node.keys()))
        return [n[0] for s, n in series2node.items() if len(n) > 1]
            

if __name__ == '__main__':
    nums = '1,2,3,4,#,2,4,#,#,4'
    root = deserialize(nums)
    solu = Solution()
    res = solu.findDuplicateSubtrees(root)
    for node in res:
        print(node)