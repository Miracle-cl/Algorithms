from typing import List
import bisect
import heapq
from collections import defaultdict, deque


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # delayed decision
        ans = []
        dry_days = []
        lake_map = {} # lake with rain in last day
        for i, lake in enumerate(rains):
            if lake > 0:
                ans.append(-1)
                if lake in lake_map:
                    if not dry_days:
                        return []
                    idx = bisect.bisect_right(dry_days, lake_map[lake])
                    # print(lake, dry_days, idx)
                    if idx >= len(dry_days):
                        return []
                    ans[dry_days[idx]] = lake
                    dry_days.pop(idx)
                lake_map[lake] = i
            else:
                dry_days.append(i)
                ans.append(-10)
        # print(ans)
        ans = [1 if a == -10 else a for a in ans]
        return ans

    def avoidFlood_heap(self, rains: List[int]) -> List[int]:
        lake_rains = defaultdict(deque)
        ans = []
        for i, lake in enumerate(rains):
            lake_rains[lake].append(i)
            ans.append(-1 if lake > 0 else -10)

        h = [] # (next rain day, lake id)
        for i, lake in enumerate(rains):
            if lake > 0:
                if len(lake_rains[lake]) > 1:
                    lake_rains[lake].popleft()
                    heapq.heappush(h, (lake_rains[lake][0], lake))
            else:
                if not h:
                    continue
                first_nxt_rain_day, lake = heapq.heappop(h)
                if first_nxt_rain_day > i:
                    ans[i] = lake
                else:
                    return []
        if h:
            return []
        ans = [1 if a == -10 else a for a in ans]
        return ans



# rains = [0,1,3,0,2,0,1,2]
# rains = [0,1,1]
rains = [2,3,0,0,3,1,0,1,0,2,2]
ss = Solution()
res1 = ss.avoidFlood(rains)
res2 = ss.avoidFlood_heap(rains)
print(res1)
print(res2)