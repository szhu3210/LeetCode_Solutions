class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0': return 0
        p1=p2=1
        for i in range(len(s))[1:]:
            p2,p1=p1,(p1 if s[i]!='0' else 0)+(p2 if 10<=int(s[i-1:i+1])<=26 else 0)
        return p1