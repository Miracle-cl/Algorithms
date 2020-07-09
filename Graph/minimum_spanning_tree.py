from typing import List
import heapq


N = 6
# (u, v, w)
edges = [(0,1,1), (0,3,4), (0,4,3), (1,3,4), (1,4,2), (2,4,4), (2,5,5), (3,4,4), (4,5,7)]


def prim(N: int, edges: List) -> int:
    adj = [[] for _ in range(N)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    q = [(0, 0)] # weight, node
    visited = [0] * N
    cost = 0
    while q:
        w, u = heapq.heappop(q)
        if visited[u]:
            continue
        cost += w
        visited[u] = 1
        # print(u)
        for v, w in adj[u]:
            if visited[v]:
                continue
            heapq.heappush(q, (w, v)) # if need edges, then (w, u, v)
    return cost


def kruskal(N: int, edges: List) -> int:
    parent = list(range(N))
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    cost = 0
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        pu, pv = find(u), find(v)
        if pu != pv: # u & v is not connected: !conn(u, v)
            cost += w
            parent[pu] = pv
            # print(u, v)
        # print(u, v, parent)
    return cost


c1 = prim(N, edges)
c2 = kruskal(N, edges)
print(c1, c2)