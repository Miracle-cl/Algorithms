from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        r, c = len(grid), len(grid[0])
        roots = list(range(r * c))
        
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]
        
        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return True
            roots[rv] = ru
            return False
        
        
        for i in range(r):
            for j in range(c):
                if j > 0 and grid[i][j-1] == grid[i][j]:
                    # merge left and it
                    v = i * c + j
                    if union(v-1, v):
                        return True
                if i > 0 and grid[i-1][j] == grid[i][j]:
                    # merge up and it
                    v = i * c + j
                    if union(v - c, v):
                        return True
        return False

    def containsCycle_1(self, grid: List[List[str]]) -> bool:
        import sys
        sys.setrecursionlimit(999999999) # default 998
        r, c = len(grid), len(grid[0])

        visited = [[0] * c for _ in range(r)]

        def dfs(i, j, pi, pj, char):
            if visited[i][j] >= 1:
                return True
            visited[i][j] = 1
            for ni, nj in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                if ni < 0 or ni >= r or nj < 0 or nj >= c or (ni == pi and nj == pj) or grid[ni][nj] != char:
                    continue
                if dfs(ni, nj, i, j, char):
                    visited[i][j] = 2
                    return True
            visited[i][j] = 2
            return False

        for i in range(r):
            for j in range(c):
                if visited[i][j] >= 1:
                    continue
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
        return False


# grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# grid = [["b","a","c"],["c","a","c"],["d","d","c"],["b","c","c"]]
ss = Solution()
res = ss.containsCycle(grid)
print(res)