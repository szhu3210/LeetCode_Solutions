class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i,x in enumerate(s):
            if x in d:
                continue
            elif s[i:].count(x)==1:
                return i
            else:
                d[x]=1
        return -1