class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q=collections.deque()
        self.size=size
        self.s=0
        
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.s+=val
        if len(self.q)>self.size:
            self.s-=self.q.popleft()
        # print self.q, self.s
        return self.s/float(len(self.q))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)