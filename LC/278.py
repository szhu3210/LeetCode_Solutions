# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        i, j = 1, n
        while (i+j)/2>i:
            if isBadVersion((i+j)/2):
                j=(i+j)/2 
            else:
                i=(i+j)/2
        return j