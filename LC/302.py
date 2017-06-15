class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        ## brute force
        # return sum('1' in r for r in image) * sum('1' in r for r in zip(*image))
        
        ## binary search
        def find(lo,hi,func):
            while lo<hi:
                mid=(lo+hi)//2
                if func(mid):
                    hi=mid
                else:
                    lo=mid+1
            return lo
        up=find(0,x,lambda i: '1' in image[i])
        down=find(x,len(image), lambda i: '1' not in image[i])
        left=find(0,y, lambda i: any('1'==row[i] for row in image))
        right=find(y,len(image[0]), lambda i: all('0'==row[i] for row in image))
        return (down-up)*(right-left)