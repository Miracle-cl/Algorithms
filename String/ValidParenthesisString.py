class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        min_cnt = 0
        max_cnt = 0
        for i, c in enumerate(s):
            if c == '(':
                min_cnt += 1
            else:
                min_cnt -= 1
            
            if c != ')':
                max_cnt += 1
            else:
                max_cnt -= 1
                
            if max_cnt < 0:
                return False
            min_cnt = max(0, min_cnt)
        return min_cnt == 0


if __name__ == '__main__':
    solu = Solution()
    # s = '((*))'
    s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    res = solu.checkValidString(s)
    print(res)
