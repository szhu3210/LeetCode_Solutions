class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l = [[1]]
        for x in range(numRows-1):
            l.append([sum(x) for x in zip([0]+l[-1], l[-1]+[0])])
        return l