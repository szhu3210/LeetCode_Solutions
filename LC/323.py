class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def root(x):
            t=x
            while t!=graph[t]:
                t=graph[t]
            graph[x]=t
            return t
        graph=range(n)
        for i,j in edges:
            graph[root(j)]=root(i)
        res=set()
        for i in range(n):
            res.add(root(i))
        return len(res)