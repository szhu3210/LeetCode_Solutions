class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        matrix={(i,j):matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))}
        length={}
        for i,j in sorted(matrix, key=matrix.get):
            length[(i,j)]=1+max([length[(a,b)] for a,b in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if (a,b) in matrix and matrix[(i,j)]>matrix[(a,b)]] or [0])
        return max(length.values() or [0])