from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        import re
        self.arr = re.split(r'([\+\-\*]+)', input)
        self.arr = [s if s in '+-*' else int(s) for s in self.arr]
        return self.helper(0, len(self.arr)-1)

    def helper(self, l, r):
        if l >= r:
            return [self.arr[l]]
        results = []
        for i in range(l, r+1):
            punc = self.arr[i]
            if isinstance(punc, str):
                lres = self.helper(l, i-1)
                rres = self.helper(i+1, r)
                for ln in lres:
                    for rn in rres:
                        results.append(self.calcurate(ln, punc, rn))
        return results

    def calcurate(self, a, p, b):
        if p == '+':
            return a + b
        elif p == '-':
            return a - b
        else:
            return a * b


inp = "2-1-1"
inp = "20*3-3*4"
s = Solution()
res = s.diffWaysToCompute(inp)
print(res)
