from typing import List
from collections import deque


class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        # visited {0: unvisited, 1: visiting, 2: visited}
        self.visited = [0] * numCourses
        for end, start in prerequisites:
            self.graph[start].append(end)
        print(self.graph)

        for i in range(numCourses):
            if not self._dfs(i):
                return False
        print(self.visited)
        return True

    def _dfs(self, start):
        if self.visited[start] == 1:
            return False
        if self.visited[start] == 2:
            return True

        self.visited[start] = 1
        for end in self.graph[start]:
            if not self._dfs(end):
                return False
        self.visited[start] = 2
        return True

    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        # visited {0: unvisited, 1: visiting, 2: visited}
        visited = [0] * numCourses
        for end, start in prerequisites:
            graph[start].append(end)
        # print(graph)
        def _dfs(start):
            if visited[start] == 1:
                return False
            if visited[start] == 2:
                return True

            visited[start] = 1
            for end in graph[start]:
                if not _dfs(end):
                    return False
            visited[start] = 2
            return True

        for i in range(numCourses):
            if not _dfs(i):
                return False
        # print(visited)
        return True

class SolutionBFS:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = [[] for _ in range(numCourses)]
    #     incnt = [0] * numCourses
    #     for end, start in prerequisites:
    #         graph[start].append(end)
    #         incnt[end] += 1

    #     q = []
    #     visited = 0
    #     for i, c in enumerate(incnt):
    #         if c == 0:
    #             q.append(i)

    #     while q:
    #         start = q.pop(0)
    #         visited += 1
    #         for end in graph[start]:
    #             incnt[end] -= 1
    #             if incnt[end] == 0:
    #                 q.append(end)
    #     return visited == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for u, v in prerequisites:
            g[u].append(v)
            indegrees[v] += 1

        q = deque([i for i in range(numCourses) if indegrees[i] == 0])
        visited = 0
        while q:
            u = q.popleft()
            visited += 1
            for v in g[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        return visited == numCourses

numCourses = 4
# prerequisites = [[0,1], [1,3], [1,2], [2,3]]
prerequisites = [[0,1], [3,1], [1,2], [2,3]]
s = SolutionDFS()
res = s.canFinish(numCourses, prerequisites)
print(res)
