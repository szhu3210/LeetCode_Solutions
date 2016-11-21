import logging
logging.basicConfig(level=logging.INFO)
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res=0
        if not matrix:
            return 0
        for row in matrix:
            logging.info( ' '+'  '.join(row))
        logging.info('--------------------')
        n=len(matrix[0])
        left=[0 for _ in xrange(n)]
        right=[n for _ in xrange(n)]
        height=[0 for _ in xrange(n)]
        area=[0 for _ in xrange(n)]
        for row in matrix:
            curLeft=0
            curRight=n-1
            for i,x in enumerate(row):
                if x=='0':
                    height[i]=0
                    left[i]=0
                    curLeft=i+1
                else:
                    height[i]=height[i]+1
                    left[i]=max(left[i], curLeft)
            for i in xrange(n-1,-1,-1):
                if row[i]=='0':
                    right[i]=n-1
                    curRight=i-1
                else:
                    right[i]=min(right[i], curRight)
                    area[i]=height[i]*(right[i]-left[i]+1)
            logging.info(left)
            logging.info(right)
            logging.info(height)
            logging.info(area)
            res=max(res,max(area))
        return res
rec=["11111111","11111110","11111110","11111000","01111000"]
print(Solution().maximalRectangle(rec))

