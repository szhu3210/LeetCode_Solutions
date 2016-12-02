class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d=len(s)-len(t)
        if d==0:
            temp=0
            for i in range(len(t)):
                if s[i]!=t[i]:
                    temp+=1
            return temp==1
        elif abs(d)==1:
            if d<0:
                s,t = t,s
            for i in range(len(t)):
                if s[i]!=t[i]:
                    return s[:i]==t[:i] and s[i+1:]==t[i:]
            return True
        else:
            return False