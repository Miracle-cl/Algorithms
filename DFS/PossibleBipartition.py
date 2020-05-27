import collections
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for i, j in dislikes:
            adj[i].append(j)
            adj[j].append(i)
            
        _colors = [0] * (1+N)
        
        def dfs(u, color):
            _colors[u] = color
            for v in adj[u]:
                if _colors[v] == color:
                    return False
                if _colors[v] == 0 and not dfs(v, -color):
                    return False
            return True
        
        for u in range(1, 1+N):
            if _colors[u] == 0 and not dfs(u, 1):
                return False
        return True

    def possibleBipartition_bfs(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for i, j in dislikes:
            adj[i].append(j)
            adj[j].append(i)
            
        _colors = [0] * (1+N)
        q = []
        for i in range(1, 1+N):
            if _colors[i] != 0:
                continue
            _colors[i] = 1
            q.append(i)
            while q:
                u = q.pop()
                color = _colors[u]
                for v in adj[u]:
                    if _colors[v] == color:
                        return False
                    if _colors[v] != 0:
                        continue
                    _colors[v] = -color
                    q.append(v)
        return True


if __name__ == '__main__':
    N = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    ss = Solution()
    r1 = ss.possibleBipartition(N, dislikes)
    r2 = ss.possibleBipartition_bfs(N, dislikes)
    print(r1, r2)