class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # 1-liner
        # return list(heapq.merge(*matrix))[k-1]
        
        # use heap
        if not any(matrix): return
        m, n = len(matrix), len(matrix[0])
        # print m, n
        h=[]
        heapq.heappush(h, (matrix[0][0], 0, 0))
        c=0
        while h and c<k:
            # print h
            res, i, j = heapq.heappop(h)
            # print res, i, j
            if j+1<n:
                # print 'push right'
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
            if j==0 and i+1<m:
                # print 'push down'
                heapq.heappush(h, (matrix[i+1][j], i+1, j))
            c+=1
        return res