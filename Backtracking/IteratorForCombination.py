import math


class CombinationIterator:

    # ===================== yield =====================
    def __init__(self, characters: str, combinationLength: int):
        n = len(characters)
        def backtrack(start, out, length):
            if length == combinationLength:
                yield out
            for i in range(start, n):
                for _ in backtrack(i+1, out+characters[i], length+1):
                    yield _
        self.gen = backtrack(0, '', 0)
        # self.cnt = math.comb(n, combinationLength)
        self.cnt = math.factorial(n) / (math.factorial(n-combinationLength) * math.factorial(combinationLength))

    def next(self) -> str:
        if self.hasNext():
            self.cnt -= 1
            return next(self.gen)
        return ''

    def hasNext(self) -> bool:
        if self.cnt > 0:
            return True
        return False


# class CombinationIterator:

#     def __init__(self, characters: str, combinationLength: int):
#         self.res = []
#         n = len(characters)
#         def backtrack(start, out, length):
#             if length == combinationLength:
#                 self.res.append(out)
#                 return
#             for i in range(start, n):
#                 backtrack(i+1, out+characters[i], length+1)
#         backtrack(0, '', 0)
#         self.res.reverse()

#     def next(self) -> str:
#         if self.hasNext():
#             return self.res.pop()
#         return ''

#     def hasNext(self) -> bool:
#         if self.res:
#             return True
#         return False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


obj = CombinationIterator('abc', 2)
for _ in range(3):
    print(obj.next())
print(obj.cnt)