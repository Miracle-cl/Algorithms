from typing import List
# from functools import lru_cache

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        def backtrack(i, j, num, row, col):
            tmp = num
            visited[i][j] = 1
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] and (not visited[ni][nj]):
                    tmp = max(tmp, backtrack(ni, nj, num+grid[ni][nj], row, col))
            visited[i][j] = 0
            return tmp

        mv = 0
        row, col = len(grid), len(grid[0])
        visited = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if not grid[i][j]:
                    continue
                res = backtrack(i, j, grid[i][j], row, col)
                mv = max(mv, res)

        return mv


if __name__ == '__main__':
    solu = Solution()
    # grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    grid = [[8,1,0,38,0,5],[0,27,18,36,8,15],[20,31,0,0,4,33],[0,0,17,13,36,0],[9,1,0,26,5,11],[0,0,19,14,24,7]]
    res = solu.getMaximumGold(grid)
    print(res)