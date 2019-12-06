from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [[i for i in range(1, n+1)]]

        tmp = []
        res = []
        def backtrack(n, k, start):
            if not k: # len(tmp) == k is slower
                res.append(tmp.copy())
                return
            for i in range(start, n+1):
                if i > n-k+1: # pruning
                    continue
                tmp.append(i)
                backtrack(n, k-1, i+1)
                tmp.pop()
        backtrack(n, k, 1)
        return res


if __name__ == '__main__':
    solu = Solution()
    n, k = 4, 2
    res = solu.combine(n, k)
    print(res)