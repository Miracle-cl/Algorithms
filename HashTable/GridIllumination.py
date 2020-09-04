from typing import List
from collections import defaultdict


class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # if (i, j) in lamps, then in x=i, y=j, x+y=i+j, x-y=i-j is illuminated 
        s = set(tuple(x) for x in lamps)
        cntx = defaultdict(int)
        cnty = defaultdict(int)
        cntmd = defaultdict(int) # Main diagonal: x+y
        cntad = defaultdict(int) # Anti-diagonal: x-y

        for x, y in lamps:
            cntx[x] += 1
            cnty[y] += 1
            cntmd[x+y] += 1
            cntad[x-y] += 1
            
        res = []
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
        for x, y in queries:
            if cntx[x] > 0 or cnty[y] > 0 or cntmd[x+y] > 0 or cntad[x-y] > 0:
                res.append(1)
            else:
                res.append(0)
            
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if (nx, ny) in s:
                    s.remove((nx, ny))
                    cntx[nx] -= 1
                    cnty[ny] -= 1
                    cntmd[nx+ny] -= 1
                    cntad[nx-ny] -= 1
                    
        return res


N = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,0]]

ss = Solution()
res = ss.gridIllumination(N, lamps, queries)
print(res)