from typing import List   

class Trie:
    def __init__(self):
        self.left = None # next is 0
        self.right = None # next is 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        
        def add(num):
            cur = root
            for i in range(31, -1, -1):
                bi = (num >> i) & 1
                if bi == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right
                
        def get_max(num):
            cur = root
            max_ = 0
            for i in range(31, -1, -1):
                bi = (num >> i) & 1
                if bi == 0:
                    if cur.right:
                        max_ = max_ * 2 + 1
                        cur = cur.right
                    else:
                        max_ *= 2
                        cur = cur.left
                else:
                    if cur.left:
                        max_ = max_ * 2 + 1
                        cur = cur.left
                    else:
                        max_ *= 2
                        cur = cur.right
            return max_
        
        n = len(nums)
        ans = 0
        for i in range(1, n):
            add(nums[i-1])
            ans = max(ans, get_max(nums[i]))

        return ans


nums = [3,10,5,25,2,8]
sol = Solution()
res = sol.findMaximumXOR(nums)
print(res)