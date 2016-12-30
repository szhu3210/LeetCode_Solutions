class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data=[[len(v), iter(v)] for v in (v1,v2) if v]
        

    def next(self):
        """
        :rtype: int
        """
        temp=self.data.pop(0)
        res=temp[1].next()
        temp[0]-=1
        if temp[0]:
            self.data.append(temp)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())