class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        i=1
        n=0
        res=[0]
        while i<=num:
            res.append(res[i-2**n]+1)
            i+=1
            if i==2**(n+1):
                n+=1
        return res