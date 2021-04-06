from typing import List
from collections import Counter
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        h = []
        res = []
        rm_set = Counter()

        for l, r, height in buildings:
            # entering
            events.append((l, height, 1))
            # leaving
            events.append((r, height, -1))
            
        # if entering, first process highest
        # if leaving, first process shortest
        events.sort(key=lambda x: (x[0], -x[1]*x[2]))
        # print(events)

        for loc, height, typ in events:
            if typ == 1:
                if not h:
                    res.append((loc, height))
                elif -h[0] < height:
                    res.append((loc, height))
                heapq.heappush(h, -height)
            else:
                # heap remove 
                rm_set[-height] += 1
                while h and rm_set[h[0]] > 0:
                    rm_set[h[0]] -= 1
                    heapq.heappop(h)

                if not h:
                    res.append((loc, 0))
                elif height > -h[0]:
                    res.append((loc, -h[0]))
            # print(loc, height, typ, h)
                    
        return res


if __name__ == '__main__':
    # buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    buildings = [[0,2,3],[2,5,3]]
    # buildings = [[0,2,3],[0,2,4]]
    sol = Solution()
    res = sol.getSkyline(buildings)
    print(res)