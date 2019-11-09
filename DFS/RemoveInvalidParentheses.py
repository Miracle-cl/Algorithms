from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = 0, 0
        for c in s:
            if c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
            elif c =='(':
                l += 1

        res = []
        self.dfs(0, l, r, s, res)
        return res

    @staticmethod
    def is_valid(s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0

    def dfs(self, start, l, r, s, res):
        if l == 0 and r == 0:
            if self.is_valid(s):
                res.append(s)
        
        for i in range(start, len(s)):
            if i != start and s[i] == s[i-1]:
                continue
            if s[i] != '(' and s[i] != ')':
                continue
            if r > 0 and s[i] == ')':
                self.dfs(i, l, r-1, s[:i]+s[i+1:], res)
            elif l > 0 and s[i] == '(':
                self.dfs(i, l-1, r, s[:i]+s[i+1:], res)



if __name__ == '__main__':
    s = "()())()"
    # s = ")())("
    solu = Solution()
    res = solu.removeInvalidParentheses(s)
    print(res)
    # Output: ["()()()", "(())()"]