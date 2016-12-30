from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]
        self.r=[]

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        l,r=self.l,self.r
        new=num
        if len(l)==len(r):
            L=-l[0] if l else None
            R= r[0] if r else None
            if L!=None and new<L:
                heappush(r,-heappushpop(l,-new))
            else:
                heappush(r,new)
        else:
            mid=heappop(r)
            if new>=mid:
                heappush(l,-mid)
                heappush(r,new)
            else:
                heappush(l,-new)
                heappush(r,mid)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        l,r=self.l,self.r
        if len(l)==len(r):
            return (r[0]-l[0])/2.0
        else:
            return r[0]*1.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()