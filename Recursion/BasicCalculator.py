

class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        mp = {}
        for i, ch in enumerate(s):
            if ch == '(':
                stk.append(i)
            elif ch == ')' and stk:
                mp[stk.pop()] = i
        # print(mp)
                
        def f(s, beg, end):
            i = beg
            sig = 1
            ret = 0
            while i <= end:
                if s[i] == ' ':
                    i += 1
                elif s[i] == '(':
                    ret += sig * f(s, i+1, mp[i]-1)
                    i = mp[i] + 1
                elif s[i] == '+':
                    sig = 1
                    i += 1
                elif s[i] == '-':
                    sig = -1
                    i += 1
                else:
                    num = 0
                    while i <= end and '0' <= s[i] <='9':
                        num = 10 * num + ord(s[i]) - ord('0')
                        i += 1
                    ret += sig * num
            return ret
        return f(s, 0, len(s)-1)

    def calculate_1(self, s: str) -> int:
        # stack
        ops = [1]
        sign = 1
        ret = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = - ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i] >= '0' and s[i] <= '9':
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += sign * num
        return ret


# s = "(1+(4+5+2)-3)+(6+8)"
s = " ( 1- (4+5+2)-3)+(6+8) "