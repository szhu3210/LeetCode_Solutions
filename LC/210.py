class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.visited=[0 for _ in range(numCourses)]
        self.res=[]
        self.graph=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            self.graph[a].append(b)
        for x in range(numCourses):
            if self.dfs(x)==-1:
                return []
        return self.res
    
    def dfs(self, x):
        if self.visited[x]!=0:
            return self.visited[x]
        self.visited[x]=-1
        for y in self.graph[x]:
            if self.dfs(y)==-1:
                return -1
        self.visited[x]=1
        self.res.append(x)
        return 1