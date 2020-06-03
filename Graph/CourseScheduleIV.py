from typing import List

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], 
                            queries: List[List[int]]) -> List[bool]:
        # floyd algo
        adj = [[False] * n for _ in range(n)]
        for i, j in prerequisites:
            adj[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])

        res = [adj[i][j] for i, j in queries]
        return res

    def checkIfPrerequisite2(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # faster
        from_to = dict()
        adj = [[] * n for _ in range(n)]
        for i, j in prerequisites:
            adj[i].append(j)

        def dfs(u):
            if u in from_to:
                return from_to[u]

            from_to[u] = {u} # if no u then miss itself
            for v in adj[u]:
                from_to[u] |= dfs(v)

            return from_to[u]

        res = [v in dfs(u) for u, v in queries]
        return res


n = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

ss = Solution()
res = ss.checkIfPrerequisite(n, prerequisites, queries)
res2 = ss.checkIfPrerequisite2(n, prerequisites, queries)
print(res, res2)
