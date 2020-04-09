import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            if head.val != root.val:
                return False
            return dfs(head.next, root.left) or dfs(head.next, root.right)
        
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if dfs(head, node):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
            
    def isSubPath1(self, head: ListNode, root: TreeNode) -> bool:
        '''TLE'''
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val:
            return  self.isSubPath(head.next, root.left) \
                    or self.isSubPath(head.next, root.right) \
                    or self.isSubPath(head, root.left) \
                    or self.isSubPath(head, root.right)
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        