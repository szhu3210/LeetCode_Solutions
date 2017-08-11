class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        def remove1digit(n):
            if n=='0':
                return '0'
            
            n=n.lstrip('0')
            
            peak=0
            for i,c in enumerate(n):
                if c>=n[peak]:
                    peak=i
                else:
                    break
            # print n, peak
            return (n[:peak]+n[peak+1:]).lstrip('0') or '0'
            
        res=num
        for _ in range(k):
            res=remove1digit(res)
        
        return res