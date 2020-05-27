# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []

    def push(self, x: int) -> None:
        if self.stk:
            min_val = self.getMin()
            min_val = min(min_val, x)
            self.stk.append((x, min_val))
        else:
            self.stk.append((x, x))

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1][0]

    def getMin(self) -> int:
        if self.stk:
            return self.stk[-1][1]