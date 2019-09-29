from collections import deque

class UndirectedGraph:
    """via BFS"""
    def __init__(self, num_node):
        self.vertex = num_node
        self.adj = [[] for _ in range(num_node)]

    def add_edge(self, i, j):
        self.adj[i].append(j)
        self.adj[j].append(i)

    def cal_connected_components(self):
        cc = []
        visited = [False] * self.vertex
        queue = deque()
        for node in range(self.vertex):
            if visited[node]:
                continue
            queue.append(node)
            visited[node] = True
            c = []
            while queue:
                u = queue.popleft()
                c.append(u)
                for v in self.adj[u]:
                    if not visited[v]:
                        queue.append(v)
                        visited[v] = True
            cc.append(c.copy())
        return cc


if __name__ == '__main__':
    ug = UndirectedGraph(10)
    # ug.add_edge(1,0)
    # ug.add_edge(2,3)
    # ug.add_edge(3,4)
    ug.add_edge(3,1)
    ug.add_edge(5,1)
    ug.add_edge(5,3)
    ug.add_edge(5,7)
    ug.add_edge(5,9)
    ug.add_edge(2,4)
    ug.add_edge(0,6)
    ug.add_edge(0,8)
    ug.add_edge(6,8)
    cc = ug.cal_connected_components()
    print(cc)
