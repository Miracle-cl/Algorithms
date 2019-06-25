from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        token = tokens.pop()
        if token in operators:
            x = self.evalRPN(tokens)
            y = self.evalRPN(tokens)
            if token == '+':
                y += x
            elif token == '-':
                y -= x
            elif token == '*':
                y *= x
            else:
                y = - ((-y) // x) if x * y < 0 else y // x
        else:
            y = int(token)
        return y

    def evalRPN_stack(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if (token == '+' or token == '-' or token == '*' or token == '/'):
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(- ((-left) // right) if left * right < 0 else left // right )
            else:
                stack.append(int(token))
            # print(stack)
        return stack[-1]


# t = ["2", "1", "+", "3", "*"]
t = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print(s.evalRPN(t.copy()))
print(s.evalRPN_stack(t.copy()))
# print(int(12 / (-11)))
