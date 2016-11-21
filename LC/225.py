class Stack(object):
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
        self.l.append(x)
        for i in range(len(self.l)-1):
            self.l.append(self.l.pop(0))

    def pop(self):
        """
        :rtype: nothing
        """
        self.l.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.l[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.l