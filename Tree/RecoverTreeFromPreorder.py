import re

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: # NO. 1028
    def recoverFromPreorder(self, S: str) -> TreeNode:
        vals = [(len(s[1]), int(s[2])) for s in re.findall(r'((-*)(\d+))', S)][::-1]
         
        def dfs(level):
            if (not vals) or vals[-1][0] != level:
                return None
            lev, val = vals.pop()
            root = TreeNode(val)
            root.left = dfs(lev+1)
            root.right = dfs(lev+1)
            return root
        
        root = dfs(0)
        return root

    def recoverFromPreorder0(self, S: str) -> TreeNode:
        def parse_str(s):
            i = 0
            size = len(s)
            level = 0
            res = []
            while i < size:
                num = ''
                while i < size and s[i].isdigit():
                    num += s[i]
                    i += 1
                res.append((int(num), level))
                level = 0
                while i < size and s[i] == '-':
                    level += 1
                    i += 1
            return res
        
        def recover(pre_nums):
            if not pre_nums:
                return None
            val, level = pre_nums[0]
            root = TreeNode(val)
            left_tree = -1
            right_tree = -1
            for i in range(1, len(pre_nums)):
                if pre_nums[i][1] == level + 1 and left_tree < 0:
                    left_tree = i
                elif pre_nums[i][1] == level + 1 and left_tree > 0:
                    right_tree = i
            if left_tree > 0 and right_tree > 0:
                root.left = recover(pre_nums[left_tree:right_tree])
                root.right = recover(pre_nums[right_tree:])
            elif left_tree > 0:
                root.left = recover(pre_nums[left_tree:])
            return root
        
        nums = parse_str(S)
        root = recover(nums)
        return root