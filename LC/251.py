class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v=vec2d
        self.x=0
        while self.x<len(vec2d) and not vec2d[self.x]:
            self.x+=1
        if self.x==len(vec2d):
            self.x=None
        self.y=0
        self.n=None

    def next(self):
        """
        :rtype: int
        """
        res=self.v[self.x][self.y]
        if self.y < len(self.v[self.x])-1:
            self.y+=1
        else:
            self.y=0
            self.x+=1
            while self.x<len(self.v) and not self.v[self.x]:
                self.x+=1
            if self.x==len(self.v):
                self.x=None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.x!=None

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())