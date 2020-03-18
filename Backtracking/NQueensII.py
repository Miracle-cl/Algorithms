class Solution:
    def totalNQueens1(self, n: int) -> int:
        _temp = []
        self.cnt = 0

        def not_valid(r, c):
            for i, j in enumerate(_temp):
                if j == c or abs(i-r) == abs(j-c):
                    return True
            return False
        
        def backtrack(r, n):
            if r >= n:
                self.cnt += 1
                return
            for c in range(n):
                if not_valid(r, c):
                    continue
                _temp.append(c)
                backtrack(r+1, n)
                _temp.pop()
        
        backtrack(0, n)
        return self.cnt

    def totalNQueens2(self, n: int) -> int:
        _temp = []

        def not_valid(r, c):
            for i, j in enumerate(_temp):
                if j == c or abs(i-r) == abs(j-c):
                    return True
            return False
        
        def backtrack(r, n):
            if r >= n:
                return 1
            cnt = 0
            for c in range(n): # column
                if not_valid(r, c):
                    continue
                _temp.append(c)
                cnt += backtrack(r+1, n)
                _temp.pop()
            return cnt

        return backtrack(0, n) 


if __name__ == '__main__':
    solu = Solution()
    # n = 4
    n = 8
    res = solu.totalNQueens2(n)
    print(res)