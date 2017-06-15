class Solution(object):
    
    def multiply1(self, A, B):

        result=[[0]*len(B[0]) for _ in xrange(len(A))]
    
        #store indexes non-zero elements in each line of B.  Checking with any() first at this point speeds up from 124ms to 96ms
        Bi=[[i for i,v in enumerate(l) if v] if any(l) else [] for l in B]
    
        for i in xrange(len(A)):
            if not any(A[i]):
                continue
            for j in xrange(len(A[0])):
                if A[i][j]:
                    for k in Bi[j]:
                        result[i][k]+=A[i][j]*B[j][k]
    
        return result
        
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(A)
        n=len(B[0])
        res=[[0]*n for _2 in range(m)]
        nB=[[i for i in range(len(B)) if B[i][j]!=0] for j in range(n)]
        
        for row in xrange(m):
            if not any(A[row]): continue
            for col in xrange(n):
                if nB[col]:
                    for key in nB[col]:
                        if A[row][key]!=0:
                            res[row][col]+=A[row][key]*B[key][col]
        return res
        