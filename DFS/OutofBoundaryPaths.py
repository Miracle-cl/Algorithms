class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        _mem = {}
        mode = 1e9 + 7
        
        def paths(s, i, j):
            if s < 0:
                return 0
            if (i < 0) or (j < 0) or (i >= m) or (j >= n):
                return 1
            if (s, i, j) in _mem:
                return _mem[(s, i, j)]
            p = paths(s-1, i, j-1) + paths(s-1, i, j+1) + paths(s-1, i-1, j) + paths(s-1, i+1, j)
            _mem[(s, i, j)] = p % mode
            return _mem[(s, i, j)]
        
        ans = paths(N, i, j)
        return int(ans)



solu = Solution()
res = solu.findPaths(36, 5, 50, 15, 3)
print(res)
