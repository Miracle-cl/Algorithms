class GraphSCC:
    def __init__(self, num_nodes):
        self.vertex = num_nodes
        self.adj = [[] for _ in range(num_nodes)]
        self.adj_reverse = [[] for _ in range(num_nodes)]

    def add_edge(self, i, j):
        self.adj[i].append(j)
        self.adj_reverse[j].append(i)

    def _fill_order(self, u, visited, stack):
        visited[u] = 1
        for v in self.adj[u]:
            if not visited[v]:
                self._fill_order(v, visited, stack)
        stack.append(u)

    def _dfs(self, u, visited, leader):
        visited[u] = 1
        leader.append(u)
        for v in self.adj_reverse[u]:
            if not visited[v]:
                self._dfs(v, visited, leader)

    def out_scc(self):
        # first dfs graph
        visited = [0] * self.vertex
        stack = []
        for i in range(self.vertex):
            if visited[i]:
                continue
            self._fill_order(i, visited, stack)

        # second dfs graph reverse
        visited = [0] * self.vertex
        scc = []
        print(stack)
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            leader = []
            self._dfs(u, visited, leader)
            scc.append(leader.copy())
        return scc


if __name__ == '__main__':
    # n = 5
    # edges = [(1,0), (0,2), (2,1), (0,3), (3,4)]
    n = 9
    edges = [(1,4), (3,0), (0,6), (6,8), (8,5), (5,7), (6,3), (2,8), (5,2), (4,7), (7,1)]

    graph_scc = GraphSCC(n)
    for e in edges:
        graph_scc.add_edge(*e)

    res = graph_scc.out_scc()
    print(res)
