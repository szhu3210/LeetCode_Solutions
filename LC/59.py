class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        M = [[None for _ in xrange(n)] for _2 in xrange(n)]  # create matrix
        m = n
        i, j = 0, 0  # set coordinate
        l = n * n
        k = 1
        while k <= l:
            # right
            while j < n and M[i][j] is None:
                M[i][j] = k
                k += 1
                j += 1
            j -= 1
            i += 1
            # down
            while i < m and M[i][j] is None:
                M[i][j] = k
                k += 1
                i += 1
            i -= 1
            j -= 1
            # left
            while j >= 0 and M[i][j] is None:
                M[i][j] = k
                k += 1
                j -= 1
            j += 1
            i -= 1
            # up
            while i >= 0 and M[i][j] is None:
                M[i][j] = k
                k += 1
                i -= 1
            i += 1
            j += 1
        return M

