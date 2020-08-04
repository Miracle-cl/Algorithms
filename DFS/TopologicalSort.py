from typing import List, Tuple
from collections import namedtuple


def topological_sort(N: int, edges: List[List[int]]) -> Tuple[bool, List]:
    # if with cycle, then False, []
    g = [[] for _ in range(N)]
    for v, u in edges: # u is after v
        g[u].append(v)

    visited = [0] * N
    sorts = []
    def dfs(u):
        print(u, visited)
        if visited[u] == 1:
            return False
        if visited[u] == 2:
            return True
        visited[u] = 1
        for v in g[u]:
            if not dfs(v):
                return False
        sorts.append(u)
        visited[u] = 2
        return True
    
    for u in range(N):
        if not dfs(u):
            return False, []
    return True, sorts[::-1]



## method 1
class TopologicalSort:
    def __init__(self, num_nodes):
        self.vertex = num_nodes
        self.adj = [[] for _ in range(num_nodes)]

    def add_edge(self, s, t):
        self.adj[s].append(t)

    def topological_sort(self):
        visited = [0] * self.vertex
        stack = []
        for u in range(self.vertex):
            self.dfs(u, visited, stack)
        return stack[::-1]

    def dfs(self, u, visited, stack):
        if visited[u]:
            return
        visited[u] = 1
        for v in self.adj[u]:
            self.dfs(v, visited, stack)
        stack.append(u)

    # def topological_sort(self):
    #     visited = [0] * self.vertex
    #     stack = []
    #     for node in range(self.vertex):
    #         if visited[node]:
    #             continue
    #         self.dfs(node, visited, stack)
    #     return stack[::-1]
    #
    # def dfs(self, u, visited, stack):
    #     visited[u] = 1
    #     for v in self.adj[u]:
    #         if not visited[v]:
    #             self.dfs(v, visited, stack)
    #     stack.append(u)



## method 2
## =========== P604, P614 ===========
# Node = namedtuple('Node', 'val color pi d f')
# color {0: white, 1: gray, 2: black}
class Node:
    def __init__(self, val, color, pi, d, f):
        self.val = val
        self.color = color
        self.pi = pi
        self.d = d
        self.f = f

class TSBOOK:
    def __init__(self, nodes):
        self.vertex = {i: Node(n, 0, '', -1, -1) for i, n in enumerate(nodes)}
        self.adj = [[] for _ in range(len(nodes))]

    def add_edge(self, s, t):
        self.adj[s].append(t)

    def topological_sort(self):
        self.dfs()
        res = sorted(self.vertex.values(), key=lambda x: x.f, reverse=True)
        # print([(x.val, x.f) for x in res])
        return [x.val for x in res]

    def dfs(self):
        time = 0
        for uid, u in self.vertex.items():
            if u.color == 0:
                time = self.dfs_visit(uid, u, time)

    def dfs_visit(self, uid, u, time):
        time += 1
        u.d = time
        u.color = 1
        for vid in self.adj[uid]:
            v = self.vertex[vid]
            if v.color == 0:
                v.pi = u
                time = self.dfs_visit(vid, v, time)
        u.color = 2
        time += 1
        u.f = time
        return time

if __name__ == '__main__':
    # ts = TopologicalSort(6)
    # # edges = [(5,2), (5,0), (4,0), (4,1), (2,3), (3,1)]
    # edges = [(5,2), (5,0), (4,0), (4,1), (2,3), (3,1), (1,2)] # not DAG 1-2-3
    # for e in edges:
    #     ts.add_edge(*e)
    # sort_res = ts.topological_sort()
    # print(sort_res)

    nodes = ['p', 'n', 'o', 's', 'm', 'r', 'y', 'v', 'x', 'w', 'z', 'u', 'q', 't']
    node2id = {n: i for i, n in enumerate(nodes)}
    edges = [(0,2), (0,3), (0,10), (1,2), (1,11), (1,12), (2,3), (2,5), (2,7),
             (3,5), (4,5), (4,8), (4,12), (5,6), (5,11), (6,7), (7,8), (7,9),
             (9,10), (11,13), (12,13)]

    ts = TopologicalSort(len(nodes))
    for e in edges:
        ts.add_edge(*e)
    print(ts.topological_sort())

    # ts_book = TSBOOK(nodes)
    # for e in edges:
    #     ts_book.add_edge(*e)
    # res = ts_book.topological_sort()
    # print([node2id[s] for s in res])
