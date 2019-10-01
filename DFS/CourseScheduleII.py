from typing import List

class SolutionDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(numCourses)]
        self.visited = [0] * numCourses
        for end, start in prerequisites:
            self.graph[start].append(end)

        self.path = []
        for i in range(numCourses):
            if not self._dfs(i):
                return []
        return self.path

    def _dfs(self, i):
        if self.visited[i] == 1:
            return False
        if self.visited[i] == 2:
            return True

        self.visited[i] = 1
        for nxt in self.graph[i]:
            if not self._dfs(nxt):
                return False
        self.visited[i] = 2
        self.path.append(i)
        return True


numCourses = 4
prerequisites = [[0,1], [1,3], [1,2], [2,3]]
# prerequisites = [[0,1], [3,1], [1,2], [2,3]]
s = SolutionDFS()
res = s.findOrder(numCourses, prerequisites)
print(res)
