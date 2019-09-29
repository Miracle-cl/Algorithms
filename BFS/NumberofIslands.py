class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## BFS
        if not grid or not grid[0]:
            return 0
        r, c = len(grid), len(grid[0])
        cnt = 0
        q = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    q.append([i, j])
                    grid[i][j] = '0'
                    while q:
                        x, y = q.pop(0)

                        if x > 0 and grid[x-1][y] == '1':
                            q.append([x-1, y])
                            grid[x-1][y] = '0'
                        if x + 1 < r and grid[x+1][y] == '1':
                            q.append([x+1, y])
                            grid[x+1][y] = '0'
                        if y > 0 and grid[x][y-1] == '1':
                            q.append([x, y-1])
                            grid[x][y-1] = '0'
                        if y + 1 < c and grid[x][y+1] == '1':
                            q.append([x, y+1])
                            grid[x][y+1] = '0'

                    cnt += 1
        return cnt



grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
