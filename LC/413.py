class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if len(A)<3:
            return 0
        
        t = []
        for i in range(2, len(A)):
            if A[i-2]-A[i-1]==A[i-1]-A[i]:
                t.append(True)
            else:
                t.append(False)
        # print t
                
        i = 0
        c = 0
        res = 0
        while i<len(t):
            if t[i]:
                c += 1
            else:
                res += ((1+c)*c)//2
                c = 0
            i += 1
        res += ((1+c)*c)//2
        
        return res