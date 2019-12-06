from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc

        def check(i, j):
            stack = [(i, j)]
            seen = {(i, j)}
            while stack:
                i, j = stack.pop()
                for ni, nj in neighbors(i, j):
                    if grid[ni][nj] == 1 and (ni, nj) not in seen:
                        stack.append((ni, nj))
                        seen.add((ni, nj))
            return len(seen), seen

        _mem = {}
        ids0 = []
        level = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in _mem:
                    area, keys = check(i, j)
                    _mem.update({k: (area, level) for k in keys})
                    level += 1
                elif grid[i][j] == 0:
                    ids0.append((i, j))
        if len(ids0) < 2:
            return n * n
        max_ans = 0
        for i, j in ids0:
            levels = set()
            ans = 0
            for ni, nj in neighbors(i, j):
                if grid[ni][nj] == 1:
                    area, level = _mem[(ni, nj)]
                    if level not in levels:
                        ans += area
                        levels.add(level)
            max_ans = max(ans+1, max_ans)
                    
        return max_ans


if __name__ == '__main__':
    grid = [[0,0,0,0,0,0,0],
            [0,1,1,1,1,0,0],
            [0,1,0,0,1,0,0],
            [1,0,1,0,1,0,0],
            [0,1,0,0,1,0,0],
            [0,1,0,0,1,0,0],
            [0,1,1,1,1,0,0]]
    solu = Solution()
    res = solu.largestIsland(grid)
    print(res)
