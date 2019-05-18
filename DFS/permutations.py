class Solution:
    def permuteUnique(self, nums):
        self.res = []
        self.temp = []
        self.nums = sorted(nums)
        self.size = len(nums)
        self.visited = [False] * self.size
        self.dfs(0)
        return self.res

    def dfs(self, tl):
        if tl == self.size:
            self.res.append(self.temp[:])
            return
        for i in range(self.size):
            if self.visited[i] or (i > 0 and self.nums[i-1] == self.nums[i] and not self.visited[i-1]):
                continue
            self.temp.append(self.nums[i])
            self.visited[i] = True
            self.dfs(tl+1)
            self.temp.pop()
            self.visited[i] = False

    def nextPermutation(self, nums):
        flag = len(nums) - 2
        last = flag + 1
        while flag >= 0 and nums[flag] >= nums[flag+1]:
            flag -= 1
        if flag >= 0:
            while nums[flag] >= nums[last]:
                last -= 1

            nums[flag], nums[last] = nums[last], nums[flag]

        return nums[:flag + 1] + list(reversed(nums[flag + 1 : ]))


nums = [1,2,3]
# nums = [1,1,2,2]
solu = Solution()
res = solu.permuteUnique(nums)
for i in range(len(res)-1):
    x = res[i]
    y = res[i+1]
    pred = solu.nextPermutation(x[:])
    # assert pred == y
    print(x, y, pred)
x = res[-1]
y = res[0]
pred = solu.nextPermutation(x[:])
print(x, y, pred)
# for sa in res:
#     print(sa)
