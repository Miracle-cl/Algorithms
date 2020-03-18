from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        _temp = []
        res = []

        def _not_valid(r, c):
            for i, j in _temp:
                if j == c or abs(i-r) == abs(j-c):
                    return True
            return False
            
        def backtrack(r, n):
            if r >= n:
                _s = [None for _ in range(n)]
                for i, j in _temp:
                    _s[i] = '.' * j + 'Q' + '.' * (n-1-j)
                res.append(_s)
                return
            for j in range(n):
                if _not_valid(r, j):
                    continue
                _temp.append((r, j))
                backtrack(r+1, n)
                _temp.pop()
                
        backtrack(0, n)
        return res


if __name__ == '__main__':
    solu = Solution()
    n = 4
    res = solu.solveNQueens(n)
    print(res)