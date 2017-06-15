# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res=[]

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        i=bisect.bisect_left(self.res, [val,val])
        
        if i>0 and self.res[i-1][1]>=val-1:
            # merge left
            self.res[i-1][1]=max(val, self.res[i-1][1])
        else:
            # no merge left, insert
            self.res.insert(i,[val,val])
            i+=1
            
        if i<len(self.res) and self.res[i][0]<=self.res[i-1][1]+1:
            # merge right
            self.res[i-1][1]=self.res[i][1]
            self.res.pop(i)
        else:
            # no merge right
            pass

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        interval=[]
        for s,e in self.res:
            interval.append(Interval(s,e))
        return interval


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()