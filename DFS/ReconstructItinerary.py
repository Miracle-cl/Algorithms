from typing import List

class S:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ap = set([a for a, _ in tickets] + [b for _, b in tickets])
        ap = sorted(ap)
        ap.remove('JFK')
        ap = ['JFK'] + ap
        print(ap)
        return ['a']



tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
res = ["JFK","ATL","JFK","SFO","ATL","SFO"]
# ["JFK","SFO","ATL","JFK","ATL","SFO"]
s = Solution()
s.findItinerary(tickets)
