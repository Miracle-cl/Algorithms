from typing import List

# Time O(9*r*c*c)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # j is loc of robot1, k is loc of robot2, i is row
        r, c = len(grid), len(grid[0])
        dp = [[[0] * c for _ in range(c)] for _ in range(r)]

        for j in range(1, c-1):
            dp[0][j][c-1] = grid[0][c-1]
        for k in range(1, c-1):
            dp[0][0][k] = grid[0][0]
        dp[0][0][c-1] = grid[0][0] + grid[0][c-1]

        def _dp(i, j, k):
            for nj in (j-1, j, j +1):
                for nk in (k-1, k, k+1):
                    if nj < 0 or nj >=c or nk < 0 or nk >= c or nj == nk:
                        yield 0
                    else:
                        yield dp[i-1][nj][nk] + grid[i][j] + grid[i][k]


        for i in range(1, r):
            for j in range(min(i+1, c)):
                for k in range(max(c-i-1, 0), c):
                    if j == k:
                        continue
                    dp[i][j][k] = max(_dp(i, j, k))

        return max(dp[r-1][j][k] for j in range(c) for k in range(c))


# grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
ss = Solution()
res = ss.cherryPickup(grid)
print(res)