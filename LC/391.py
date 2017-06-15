class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # check vertex: iter through all rectangles and use a set to keep track of coordinates. if overlapped, cancel out, else add.
        # sum up areas at the same time.
        vertex = set()
        area = 0
        for a,b,c,d in rectangles:
            v = [(a,b), (c,d), (a,d), (c,b)] # 4 points of a rectangle
            for p in v:
                # p is a point
                if p in vertex:
                    vertex.remove(p)
                else:
                    vertex.add(p)
            area += (c-a)*(d-b)
        
        # check remaining points: must be 4 points left and can form a rectangle.
        if len(vertex)!=4:
            return False
        vertex = sorted(list(vertex))
        a,b = vertex[0]
        c,d = vertex[-1]
        if vertex[1]==(a,d) and vertex[2]==(c,b):
            pass
        else:
            return False
        
        # check area: must be equal to sum of areas of small rectangles.
        return area==(d-b)*(c-a)
        