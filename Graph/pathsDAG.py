# DAG

def find_all_path(n, adj_list):
    adj = [[] for _ in range(1+n)]
    non_begins = set()
    for i, j in adj_list:
        adj[i].append(j)
        non_begins.add(j)
        
    begins = [i for i in range(1, 1+n) if i not in non_begins]
    paths = []

    def dfs(u):
        if not adj[u]:
            paths.append(tmp[:])
            return
        for v in adj[u]:
            tmp.append(v)
            dfs(v)
            tmp.pop()

    for b in begins:
        tmp = [b]
        dfs(b)

    return paths


n = 6
adj_list = [[4,6],[4,3],[3,6],[3,2],[1,2],[6,1],[6,5]]
res = find_all_path(n, adj_list)
print(res)