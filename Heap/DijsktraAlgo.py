import heapq

# BFS, no negative weight, directed graph
# O(E + VlogV)

class DijsktraAlgorithm:
    def __init__(self, vertex):
        self.vertex = vertex

    def mkr_adj_list(self, inputs):
        # here inputs: x -> y and y -> x
        adj = [[] for _ in range(self.vertex)]
        weights = [[] for _ in range(self.vertex)]

        for x, y, w in inputs:
            adj[x].append(y)
            adj[y].append(x)
            weights[x].append(w)
            weights[y].append(w)
        return adj, weights

    def dijsktra_list(self, src, inputs):
        adj, weights = self.mkr_adj_list(inputs)

        dist = [float('inf') for _ in range(self.vertex)]
        dist[src] = 0

        h = []
        heapq.heappush(h, (0, src)) # (weight, node)
        while h:
            _, u = heapq.heappop(h)
            for i, v in enumerate(adj[u]):
                w = weights[u][i]
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(h, (w, v))
        return dist

    def mkr_adj_matrix(self, inputs):
        # here inputs: x -> y and y -> x
        adj_weight = [[0] * self.vertex for _ in range(self.vertex)]
        for x, y, w in inputs:
            adj_weight[x][y] = w
            adj_weight[y][x] = w
        return adj_weight

    def dijsktra_matrix(self, src, inputs):
        adj_weight = self.mkr_adj_matrix(inputs)

        dist = [float('inf') for _ in range(self.vertex)]
        dist[src] = 0

        h = []
        heapq.heappush(h, (0, src)) # (weight, node)
        while h:
            _, u = heapq.heappop(h)
            for v, w in enumerate(adj_weight[u]):
                if w and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(h, (w, v))
        return dist


if __name__ == '__main__':
    inputs = [(0,1,1), (0,2,4), (1,2,2), (1,3,7), (1,4,5), (2,4,1), (3,4,3), (3,5,2), (4,5,6)]
    src = 0
    da1 = DijsktraAlgorithm(6)
    d1_list = da1.dijsktra_list(src, inputs)
    d1_matrix = da1.dijsktra_matrix(src, inputs)
    print(d1_list)
    print(d1_matrix)
