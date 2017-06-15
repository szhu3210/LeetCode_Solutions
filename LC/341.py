# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack=[nestedList]
        self.buf=None
        self.findNext()
    
    def findNext(self):
        if not self.stack: 
            self.buf=None
            return
        if self.stack[-1]:
            t=self.stack[-1].pop(0)
            if t.isInteger():
                self.buf=t.getInteger()
            else:
                self.stack.append(t.getList())
                self.findNext()
        else:
            self.stack.pop()
            self.findNext()
        
    def next(self):
        """
        :rtype: int
        """
        res=self.buf
        self.findNext()
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buf!=None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())