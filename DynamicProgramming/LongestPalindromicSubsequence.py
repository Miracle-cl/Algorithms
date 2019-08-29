from functools import lru_cache
import time

class Solution:
    @lru_cache(maxsize=None)
    def longestPalindromeSubseq(self, s):
        if len(s) == 1 or (len(s) == 2 and s[0] != s[1]):
            return 1
        elif len(s) == 2 and s[0] == s[1]:
            return 2
        if s[0] == s[-1]:
            return self.longestPalindromeSubseq(s[1:-1]) + 2
        else:
            return max(self.longestPalindromeSubseq(s[:-1]), self.longestPalindromeSubseq(s[1:]))

    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n-length, -1, -1):
                j = i + length - 1
                # print(i, j)
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # print(dp)
        return dp[0][n-1]

    def longestPalindromeSubseq3(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp_0 = [0] * n
        dp_1 = [0] * n
        dp_2 = [0] * n
        for length in range(1, n + 1):
            for i in range(n-length, -1, -1):
                j = i + length - 1
                # print(i, j)
                if i == j:
                    dp_0[i] = 1
                else:
                    if s[i] == s[j]:
                        dp_0[i] = dp_2[i+1] + 2
                    else:
                        dp_0[i] = max(dp_1[i], dp_1[i+1])
            print(dp_0, dp_1, dp_2)
            dp_2 = dp_1[:]
            dp_1 = dp_0[:]
        # print(dp)
        return dp_0[0]



s = 'bbbcb'
t0 = time.time()
x = Solution()
# res = x.longestPalindromeSubseq(s)
# res1 = x.longestPalindromeSubseq2(s)
res1 = x.longestPalindromeSubseq3(s)
# print(res)
print(res1)
print(time.time() - t0)
