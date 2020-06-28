from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 1 + len(edges)
        parents = list(range(n))
        # ranks = [0] * n
        
        def _find(i):
            if i != parents[i]:
                parents[i] = _find(parents[i])
            return parents[i]
        
        def _union(u, v):
            pu, pv = _find(u), _find(v)
            if pu == pv:
                return False
            parents[pu] = pv
            return True
            
        for edge in edges:
            if not _union(edge[0], edge[1]):
                return edge
        return []


edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]