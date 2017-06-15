class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph=[set() for _ in range(n)]
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        leaves=[i for i,adj in enumerate(graph) if len(adj)==1]
        
        while n>2:
            n-=len(leaves)
            new_leaf=[]
            for leaf in leaves:
                adj=graph[leaf].pop()
                graph[adj].remove(leaf)
                if len(graph[adj])==1: new_leaf.append(adj)
            leaves=new_leaf
        return leaves or [0]
        