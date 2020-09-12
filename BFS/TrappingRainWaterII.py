from typing import List
from heapq import heappush, heappop


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        r, c = len(heightMap), len(heightMap[0])
        if r < 3 or c < 3:
            return 0

        vis = [[0] * c for _ in range(r)]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        h = []

        for i in range(r):
            heappush(h, (heightMap[i][0], i, 0))
            heappush(h, (heightMap[i][c-1], i, c-1))
            vis[i][0] = vis[i][c-1] = 1
            
        for j in range(1, c-1):
            heappush(h, (heightMap[0][j], 0, j))
            heappush(h, (heightMap[r-1][j], r-1, j))
            vis[0][j] = vis[r-1][j] = 1

        ans = 0
        mh = 0
        while h:
            height, i, j = heappop(h)
            mh = max(mh, height)
            for dx, dy in dirs:
                nx, ny = i+dx, j+dy
                if nx < 0 or nx >= r or ny < 0 or ny >= c or vis[nx][ny]:
                    continue
                if heightMap[nx][ny] < mh:
                    ans += mh - heightMap[nx][ny]
                heappush(h, (heightMap[nx][ny], nx, ny))
                vis[nx][ny] = 1
                
        return ans


heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
res = Solution().trapRainWater(heightMap)
print(res)