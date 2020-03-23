from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (not matrix) or (not matrix[0]):
            return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0] * c for _ in range(r)]
        max_v = 0
        for j in range(c):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                max_v = 1
        for i in range(1, r):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                max_v = 1
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                max_v = max(max_v, dp[i][j])
        # print(dp)
        return max_v * max_v


if __name__ == '__main__':
    solu = Solution()
    # matrix = [["1","0","1","0","0"]]
    # matrix = [['1'], ['1']]
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
              ["1","1","1","1","1"],["1","0","0","1","0"]]
    res = solu.maximalSquare(matrix)
    print(res)

