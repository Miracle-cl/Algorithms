from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        # find longest common prefix and suffix of s + rev_s
        _s = s + rev_s
        nxt = self.build(s)
        j = 0
        for i in range(n, 2*n):
            while j > 0 and _s[i] != _s[j]:
                j = nxt[j]
            if _s[i] == _s[j]:
                j += 1
            nxt.append(j)
            # print(i, j)
        # print(nxt)
        return rev_s[:n-nxt[-1]] + s

    def shortestPalindrome_1(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        # find longest common prefix and suffix of s + rev_s
        _s = s + '#' + rev_s # avoid common prefix and suffix inclued s and rev_s
        nxt = self.build(_s)
        return rev_s[:n-nxt[-1]] + s

    @staticmethod
    def build(p: str) -> List[str]:
        # nxt[i]: length of longest prefix of p[:i] that is also the suffix
        # len(nxt) = len(p) + 1
        nxt = [0, 0]
        j = 0
        for i in range(1, len(p)):
            while j > 0 and p[i] != p[j]: # fail then jump until a match or j == 0
                j = nxt[j]
            if p[i] == p[j]:
                j += 1
            nxt.append(j)
        return nxt


# s = "aacecaaa"
s = "aabba"
# s = "aaaaa"
# s = 'a'
ss = Solution()
res = ss.shortestPalindrome_1(s)
print(res)