from heapq import heappush, heappop
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        init_v = n * n
        path = [[init_v] * n for _ in range(n)]
        path[0][0] = grid[0][0]
        q = []
        heappush(q, (grid[0][0], 0, 0))
        while q:
            w, i, j = heappop(q)
            for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue
                nw = max(w, grid[ni][nj])
                if nw < path[ni][nj]:
                    path[ni][nj] = nw
                    heappush(q, (nw, ni, nj))

        return path[-1][-1]


if __name__ == '__main__':
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    solu = Solution()
    res = solu.swimInWater(grid)
    print(res)