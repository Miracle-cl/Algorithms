class Solution:
    def __init__(self):
        self.temp = []
        self.res = []

    def isPalindrome(self, substr):
        if substr[:] == substr[::-1]:
            return True
        else:
            return False

    def dfs(self, start):
        if (start == len(self.s)):
            # why temp[:] differences between deep copy and shallow copy
            self.res.append(self.temp[:])
        else:
            for i in range(start, len(self.s)):
                if self.isPalindrome(self.s[start:i+1]):
                    self.temp.append(self.s[start:i+1])
                    self.dfs(i+1)
                    self.temp.pop()

    def partition(self, s):
        self.s = s
        self.dfs(0)
        return self.res

s = "cdd"
solu = Solution()
result = solu.partition(s)
print(result) # [['c', 'd', 'd'], ['c', 'dd']]
