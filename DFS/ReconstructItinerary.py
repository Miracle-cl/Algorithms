from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for f, t in tickets:
            heappush(adj_list[f], t)

        routes = []
        self.dfs('JFK', adj_list, routes)
        return routes[::-1]

    def dfs(self, start, adj_list, routes):
        dests = adj_list[start]
        while dests:
            dest = heappop(dests)
            self.dfs(dest, adj_list, routes)
        routes.append(start)


if __name__ == '__main__':
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"],["JFK","ABC"]]
    s = Solution()
    res = s.findItinerary(tickets)
    print(res)
