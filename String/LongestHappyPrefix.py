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

    def longestPrefix_1(self, s: str) -> str:
        # Rabin-Karp algorithm
        base = 31
        mode = 10**9 + 7
        nums = [ord(c) - ord('a') for c in s]
        prefix = suffix =  0
        n = len(s)
        sp = 1
        max_len = 0
        for i in range(n-1):
            prefix = (prefix * base + nums[i]) % mode
            suffix = (suffix + nums[n-1-i] * sp) % mode
            sp = (sp * base) % mode
            if prefix == suffix and s[:i+1] == s[-i-1:]:
                max_len= max(max_len, i+1)
        return s[:max_len]


s = 'ababab'
solu = Solution()
res = solu.longestPrefix(s)
# res = solu.longestPrefix_1(s)
print(res)