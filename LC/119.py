class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [1]
        for x in range(rowIndex):
            l.insert(0, 1)
            for i in range(1,len(l)-1):
                l[i]+=l[i+1]
        return l