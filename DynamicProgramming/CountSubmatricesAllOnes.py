from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        height = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    height[i][j] = 1 if i == 0 else (height[i-1][j] + 1)

        res = 0
        for i in range(r):
            for j in range(c):
                if not height[i][j]:
                    continue
                h = height[i][j]
                for k in range(j, -1, -1):
                    h = min(h, height[i][k])
                    res += h
                    if not h:
                        break
        return res


mat = [[0,1,1,0],
      [0,1,1,1],
      [1,1,1,0]]
ss = Solution()
res = ss.numSubmat(mat)
print(res)