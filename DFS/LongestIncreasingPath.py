from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if (not matrix) or (not matrix[0]):
            return 0
        row, col = len(matrix), len(matrix[0])
        paths = [[0] * col for _ in range(row)]
        max_len = 1
        for i in range(row):
            for j in range(col):
                max_len = max(max_len, self.dfs(i, j, row, col, matrix, paths))
        # print(paths)
        return max_len

    def dfs(self, i, j, row, col, matrix, paths):
        if paths[i][j] > 0:
            return paths[i][j]
        tmp = 1
        for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if (0 <= ni < row) and (0 <= nj < col) and (matrix[ni][nj] < matrix[i][j]):
                tmp = max(tmp, self.dfs(ni, nj, row, col, matrix, paths)+1)

        paths[i][j] = tmp
        return tmp

    # def dfs(self, i, j, row, col, matrix, paths):
    #     if paths[i][j] > 0:
    #         return paths[i][j]
    #     left, right, up, down = 1, 1, 1, 1

    #     if i > 0 and i < row and matrix[i-1][j] < matrix[i][j]:
    #         left = self.dfs(i-1, j, row, col, matrix, paths) + 1
    #     if i >= 0 and i < row-1 and matrix[i+1][j] < matrix[i][j]:
    #         right = self.dfs(i+1, j, row, col, matrix, paths) + 1
    #     if j > 0 and j < col and matrix[i][j-1] < matrix[i][j]:
    #         up = self.dfs(i, j-1, row, col, matrix, paths) + 1
    #     if j >= 0 and j < col-1 and matrix[i][j+1] < matrix[i][j]:
    #         down = self.dfs(i, j+1, row, col, matrix, paths) + 1
    #     paths[i][j] = max(left, right, up, down)
    #     return paths[i][j]



if __name__ == '__main__':
    solu = Solution()
    matrix = [[9,9,4],
              [6,6,8],
              [2,1,1]] 
    res = solu.longestIncreasingPath(matrix)
    print(res)