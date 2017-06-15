class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not any(matrix):
            return []
        m, n = len(matrix), len(matrix[0])
        P=[[0 for j in xrange(n)] for i in xrange(m)] # the marker for Pacific
        A=[[0 for j in xrange(n)] for j in xrange(m)] # the marker for Atlantic
        
        # bfs
        def bfs(O, q):
            q=collections.deque(q)
            while q:
                i,j = q.popleft()
                O[i][j]=1
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for ii,jj in directions:
                    ni, nj = i+ii, j+jj
                    if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>=matrix[i][j] and O[ni][nj]==0:
                        O[ni][nj]=1
                        q.append((ni,nj))
        
        qA=[(0,j) for j in xrange(1,n)]+[(i,0) for i in xrange(m)]
        bfs(A,qA)
        qP=[(m-1,j) for j in xrange(0,n-1)]+[(i,n-1) for i in xrange(m)]
        bfs(P,qP)
        
        res=[]
        for i in range(m):
            for j in range(n):
                if P[i][j]==1 and A[i][j]==1:
                    res.append([i,j])
        return res