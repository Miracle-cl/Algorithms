# travelling salesman problem


def min_cost(edges):
    # len(edges)
    n_node = 5
    adj = [[float('inf')] * n_node for _ in range(n_node)]
    for u, v, w in edges:
        adj[u][v] = w
        
    states = 1 << n_node
        
    dp = [[float('inf')] * n_node for _ in range(states)]
    dp[0][0] = 0
    # get min cost of dp[31][0]

    for s in range(1, states):
        for u in range(n_node):
            for v in range(n_node):
                if (s >> v) & 1 == 0:
                    # v is visited
                    continue
                dp[s][v] = min(dp[s][v], dp[s - (1<<v)][u] + adj[u][v])
                
    return dp[states-1][0]


edges = [[0, 1, 3], [1, 2, 5], [2, 3, 5], [3, 4, 3], [4, 0, 7], [4, 1, 6], [0, 3, 4], [2, 0, 4]]
print(min_cost(edges))