from typing import List
from pprint import pprint
from collections import deque
import heapq, math
import bisect


matrix = [["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]]

r, c = len(matrix), len(matrix[0])

left = [[0] * c for _ in range(r)]
for i in range(r):
    left[i][0] = 1 if matrix[i][0] == '1' else 0
    for j in range(1, c):
        if matrix[i][j] == '1':
            left[i][j] = left[i][j-1] + 1

ans = 0
for i in range(r):
    for j in range(c):
        if left[i][j] == 0:
            continue
        width = left[i][j]
        for k in range(i-1, -1, -1):
            width = min(width, left[k][j])
            if width == 0:
                break
            ans = max(ans, width * (i - k + 1))


pprint(ans)