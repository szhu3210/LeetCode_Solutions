class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g = sorted(g)
        s = sorted(s)[::-1]
        
        for c in g:
            while s:
                if c<=s.pop():
                    res += 1
                    break
        return res