class Solution:
    def longestPrefix(self, s: str) -> str:
        nxt = [0, 0]
        n = len(s)
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = nxt[j]
            if s[i] == s[j]:
                j += 1
            nxt.append(j)
        return s[:nxt[n]]


s = 'ababab'
solu = Solution()
res = solu.longestPrefix(s)
print(res)