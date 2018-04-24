## Deep-First Search ##

class Solution(object):
    def __init__(self, candidates, target):
        super(Solution, self).__init__()
        self.candidates = candidates
        self.target = target
        self.result = []

    def combinationSum(self):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(self.candidates)
        self.dfs(self.candidates, self.target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, val):
        if target == 0:
            self.result.append(val)
        else:
            for i in range(start, len(candidates)):
                if target < 0:
                    break
                self.dfs(candidates, target-candidates[i], i, val + [candidates[i]])

s = Solution([2,3,6,7], 7)
print(s.combinationSum())

## ===================================================================================

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        curr = []
        ans = []
        def dfs(candidates, target, start, curr, ans):
            if target == 0:
                ans.append(curr[:]) # be mindful of the syntax
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target: break
                curr.append(candidates[i])
                dfs(candidates, target-candidates[i], i, curr,ans)
                curr.pop()

        dfs(candidates, target, 0, curr, ans)
        return ans

n = Solution()
print(n.combinationSum([1,2,3], 4))
