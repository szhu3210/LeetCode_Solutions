class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        save = [self.distance(tree, nut)-self.distance(squirrel, nut) for nut in nuts]
        i = save.index(max(save))
        # print nuts
        # print i
        first = nuts.pop(i)
        res = self.distance(first, squirrel) + self.distance(first, tree)
        
        for nut in nuts:
            res += self.distance(nut, tree) * 2
            
        return res
        
    def distance(self, a, b):
        ax, ay = a
        bx, by = b
        return abs(bx-ax)+abs(by-ay)