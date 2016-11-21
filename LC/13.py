class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        m=dict['I']
        p=1
        
        for x in s[::-1]:
            if (dict[x] < m and x in {'I','X','C'}):
                p=-1
            else:
                m=dict[x]
                p=1
            res+=p*dict[x]
        return res