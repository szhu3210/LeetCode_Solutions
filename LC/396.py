class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s=sum([i*x for i,x in enumerate(A)]) if A else 0
        t=sum(A)
        n=len(A)
        res=s
        A=A[::-1]
        for x in range(0,len(A)):
            s=s-n*A[x]+t
            res=max(res,s)
        return res
        