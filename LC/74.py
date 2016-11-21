class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        if m * n == 0:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        i = 0
        j = len(matrix) - 1
        if target>=matrix[-1][0]:
            return self.searchList(matrix[-1], target)
        while i < j - 1:
            mid = (i + j) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                i = mid
            else:
                j = mid
        return self.searchList(matrix[i], target)

    def searchList(self, l, t):
        i = 0
        j = len(l) - 1
        while i <= j:
            m = (i + j) // 2
            if l[m] == t:
                return True
            if l[m] > t:
                j = m - 1
            else:
                i = m + 1
        return False

