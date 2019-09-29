from typing import List
from collections import deque

class SolutionDFS:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        max_area = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                self.area = 0
                self._dfs(i, j, r, c, grid)
                max_area = max(max_area, self.area)
        return max_area

    def _dfs(self, i, j, r, c, grid):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.area += 1
        self._dfs(i-1, j, r, c, grid)
        self._dfs(i+1, j, r, c, grid)
        self._dfs(i, j-1, r, c, grid)
        self._dfs(i, j+1, r, c, grid)


class SolutionBFS:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        max_area = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                area = self._bfs(i, j, r, c, grid)
                max_area = max(max_area, area)
        return max_area

    def _bfs(self, i, j, r, c, grid):
        if grid[i][j] == 0:
            return 0
        q = deque([(i, j)])
        grid[i][j] = 0
        area = 1
        while q:
            x, y = q.popleft()
            if x > 0 and grid[x-1][y] == 1:
                q.append((x-1, y))
                grid[x-1][y] = 0
                area += 1
            if x + 1 < r and grid[x+1][y] == 1:
                q.append((x+1, y))
                grid[x+1][y] = 0
                area += 1
            if y > 0 and grid[x][y-1] == 1:
                q.append((x, y-1))
                grid[x][y-1] = 0
                area += 1
            if y + 1 < c and grid[x][y+1] == 1:
                q.append((x, y+1))
                grid[x][y+1] = 0
                area += 1
        return area


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = SolutionBFS()
ma = s.maxAreaOfIsland(grid)
print(ma)
