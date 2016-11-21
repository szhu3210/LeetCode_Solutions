class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        while(s[-1]==' ' if s else False):
            s=s[:-1]
        for i,x in enumerate(s[::-1]):
            if x==' ':
                return i
        return len(s)