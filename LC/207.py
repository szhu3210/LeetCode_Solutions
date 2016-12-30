class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        self.valid = [None for _ in range(numCourses)]
        for pr in prerequisites:
            graph[pr[0]].append(pr[1])
        for i in range(len((graph))):
            if not self.dfs(graph, i):
                return False
        return True

    def dfs(self, graph, i):
        if self.valid[i] != None:
            return self.valid[i]
        self.valid[i] = False
        for p in graph[i]:
            if not self.dfs(graph, p):
                return False
        self.valid[i] = True
        return True