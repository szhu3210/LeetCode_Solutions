class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h=len(haystack)
        n=len(needle)
        for x in range(h-n+1):
            if haystack[x:x+n] == needle:
                return x
        return -1