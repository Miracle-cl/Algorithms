from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        # print(r, c)

        def disconnected():
            cnt = 0
            visited = [[0] * c for _ in range(r)]

            def dfs(i, j):
                if i<0 or i>=r or j<0 or j>=c or not grid[i][j] or visited[i][j]:
                    return
                visited[i][j] = 1
                for ni, nj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                    dfs(ni, nj)
    
            for i in range(r):
                for j in range(c):
                    if grid[i][j] and not visited[i][j]:
                        dfs(i, j)
                        cnt += 1
                    if cnt > 1:
                        return True
            return False if cnt else True # cnt == 0

        if disconnected():
            return 0

        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    grid[i][j] = 0
                    if disconnected():
                        return 1
                    grid[i][j] = 1
        return 2


grid = [[0,0,0],[0,1,0],[0,0,0]]
# grid = [[1,0],[1,1]]