class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c=[[0,0] for _ in range(300)]

    def hit(self, t):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        c=self.c
        i=t%300
        j=t//300
        if c[i][0]==j:
            c[i][1]+=1
        else:
            c[i][0]=j
            c[i][1]=1

    def getHits(self, t):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res=0
        for i in range(len(self.c)):
            j, count = self.c[i]
            if j*300+i>t-300:
                res+=count
        return res

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)