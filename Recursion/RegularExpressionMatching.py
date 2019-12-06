import re
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool: # 36ms
        _mem = {}
        
        def recursive(s, p):
            if not p:
                return not s
            
            if (s, p) in _mem:
                return _mem[(s, p)]

            first_match = (s and (p[0] == s[0] or p[0] == '.'))

            if len(p) > 1 and p[1] == '*':
                _mem[(s, p)] = recursive(s, p[2:]) or (first_match and recursive(s[1:], p))
            else:
                _mem[(s, p)] = first_match and recursive(s[1:], p[1:])
            return _mem[(s, p)]
        
        return recursive(s, p)

    @lru_cache(maxsize=128)
    def isMatch1(self, s: str, p: str) -> bool: # 32ms
        if not p:
            return not s
        
        first_match = (s and (p[0] == s[0] or p[0] == '.'))
        
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])

    def isMatch2(self, s: str, p: str) -> bool: # 60ms
        return re.fullmatch(p, s) is not None

    def isMatch3(self, s: str, p: str) -> bool: # 1000ms
        if not p:
            return not s
        
        first_match = (s and (p[0] == s[0] or p[0] == '.'))
        
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    s = "mississippi"
    p = "mis*is*p*."
    # s = "mississsppi"
    # p = "mis*is*p*."
    # s = "aab"
    # p = "c*a*b"
    # s = "ab"
    # p = ".*"
    solu = Solution()
    res = solu.isMatch(s, p)
    print(res)