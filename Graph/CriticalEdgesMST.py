from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # (u, v, w, edge_id)
        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda x: x[2])
        
        def kruskal(exclude=-1, inclued=-1):
            parent = list(range(n))
            def find(x):
                if x != parent[x]:
                    parent[x] = find(parent[x])
                return parent[x]

            cost = 0
            e_cnt = 0
            if inclued >= 0:
                u, v, w, _ = edges[inclued]
                # pu, pv = find(u), find(v)
                parent[u] = v
                cost += w
                e_cnt += 1

            for i, (u, v, w, _) in enumerate(edges):
                if i == exclude:
                    continue
                pu, pv = find(u), find(v)
                if pu == pv:
                    continue
                cost += w
                parent[pu] = pv
                e_cnt += 1
            return cost if e_cnt == n-1 else float('inf')

        critical, pseudo_critical = [], []

        min_cost = kruskal()
        for i in range(len(edges)):
            if kruskal(exclude=i) > min_cost:
                critical.append(edges[i][3])
            elif kruskal(inclued=i) == min_cost:
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]


n = 6
edges = [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]
# n=4
# edges=[[0,1,1],[0,3,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1]]
# n=4
# edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# n=5
# edges=[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

ss = Solution()
res = ss.findCriticalAndPseudoCriticalEdges(n, edges)
print(res)