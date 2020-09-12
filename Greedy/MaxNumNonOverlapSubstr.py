from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        left = [n] * 26 # float('inf')
        right = [-1] * 26
        for i, c in enumerate(s):
            ci = ord(c) - ord('a')
            left[ci] = min(left[ci], i)
            right[ci] = max(right[ci], i)
        # print(left)

        def extend(i: int) -> int:
            p = right[ord(s[i]) - ord('a')]
            j = i
            while j <= p:
                cj = ord(s[j]) - ord('a')
                if left[cj] < i:
                    return -1
                p = max(p, right[cj])
                j += 1
            return p

        res = []
        last = -1
        for i, c in enumerate(s):
            ci = ord(c) - ord('a')
            if i != left[ci]:
                continue
            p = extend(i)
            if p == -1:
                continue
            if i > last:
                res.append('')
            res[-1] = s[i: p+1]
            last = p
            # print([i, p, s[i: p+1]])
        return res


# s = "bbcacbaba"
s = "adefaddaccc"
solu = Solution()
res = solu.maxNumOfSubstrings(s)
print(res)
