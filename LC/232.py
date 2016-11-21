class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l=[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        temp=[]
        for i in xrange(len(self.l)):
            temp.append(self.l.pop(0))
        temp.append(x)
        for i in temp[::-1]:
            self.l.insert(0,i)

    def pop(self):
        """
        :rtype: nothing
        """
        self.l.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.l[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.l