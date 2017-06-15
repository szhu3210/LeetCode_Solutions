class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        l = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                # for each element, cal sum and index and store value
                sum = i+j
                index = j if sum%2==0 else -j
                value = matrix[i][j]
                l.append((sum, index, value))
        l.sort()
        return map(lambda x: x[2], l)