from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        _mem = {}

        def f(x1, y1, x2):
            y2 = x1 + y1 - x2 
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                return -1
            if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return -1
            if x1 == 0 and y1 == 0:
                return grid[x1][y1]
            if (x1, y1, x2) in _mem:
                return _mem[x1, y1, x2]
            ans = max(f(x1-1, y1, x2-1), f(x1-1, y1, x2), 
                      f(x1, y1-1, x2-1), f(x1, y1-1, x2))
            if ans < 0:
                _mem[x1, y1, x2] = -1
                return -1
            ans += grid[x1][y1]
            if x1 != x2:
                ans += grid[x2][y2]
            _mem[x1, y1, x2] = ans
            # print(x1, y1, x2, y2, ans)
            return ans
        ans = f(n-1, n-1, n-1)
        return 0 if ans < 0 else ans

grid = [[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]

# grid = [[1, 1, -1],
#  [1, -1, 1],
#  [-1, 1,  1]]

ss = Solution()
res = ss.cherryPickup(grid)
print(res)