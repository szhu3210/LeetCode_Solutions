class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        la = len(a)
        lb = len(b)
        if la!=lb:
            return max(la, lb)
        if a!=b:
            return la
        else:
            return -1