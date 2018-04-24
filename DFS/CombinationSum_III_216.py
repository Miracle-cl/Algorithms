class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(0, 0, 0, [], k, n)
        return self.result

    def dfs(self, start, cnt, sums, nums, k, n):
        if cnt > k or sums > n:
            return
        if cnt == k and sums < n:
            return
        if cnt == k and sums == n:
            self.result.append(nums)
            return
        for x in range(start+1, 10):
            self.dfs(x, cnt+1, sums+x, nums+[x], k, n)

n = Solution()
print(n.combinationSum3(3,7))
print(n.combinationSum3(3,9))
