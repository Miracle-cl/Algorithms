from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        row, col = len(matrix), len(matrix[0])

        p = [[0] * col for _ in range(row)] # arrive loc from p if 1
        a = [[0] * col for _ in range(row)] # arrive loc from a if 1
        
        res = []

        for i in range(row):
            self.dfs(-1, i, 0, row, col, matrix, p)
            self.dfs(-1, i, col-1, row, col, matrix, a)

        for j in range(1, col):
            self.dfs(-1, 0, j, row, col, matrix, p)
            self.dfs(-1, row-1, j-1, row, col, matrix, a)

        for i in range(row):
            for j in range(col):
                if p[i][j] and a[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, val, i, j, row, col, matrix, visited):
        if i < 0 or i >= row or j < 0 or j >= col or matrix[i][j] < val or visited[i][j]:
            return
        visited[i][j] = 1
        self.dfs(matrix[i][j], i-1, j, row, col, matrix, visited)
        self.dfs(matrix[i][j], i+1, j, row, col, matrix, visited)
        self.dfs(matrix[i][j], i, j-1, row, col, matrix, visited)
        self.dfs(matrix[i][j], i, j+1, row, col, matrix, visited)


if __name__ == '__main__':
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    solu = Solution()
    res = solu.pacificAtlantic(matrix)
    print(res)