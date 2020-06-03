# Floyd-Warshall Algorithm
# Time O(n3), Space O(n2)
from typing import List


def floyd_algo(n: int, edge_weight: List[List[int]]) -> List[List[int]]:
    # return minimun weight between two nodes
    adj = [[float('inf')] * n for _ in range(n)]
    for s, e, w in edge_weight:
        adj[s][e] = w

    for i in range(n):
        adj[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])
    return adj


n = 4
edge_weight = [[0,1,3], [1,0,2], [2,1,1], [0,3,5], [3,2,2], [1,3,4]]

res = floyd_algo(n, edge_weight)
print(res)