class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = s*2
        l = len(s)
        for i in range(1,l):
            if l%i==0:
                if t[i:i+l]==s:
                    return True
        return False