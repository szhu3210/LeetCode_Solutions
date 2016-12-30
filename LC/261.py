class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges)!=n-1:
            return False
        t=range(n)
        def root(x):
            while t[x]!=x:
                x=t[x]
            return x
        for a,b in edges:
            a=root(a)
            b=root(b)
            if a==b:
                return False
            t[b]=a # union
        return True
                