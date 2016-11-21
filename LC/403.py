class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        return self.tryCross(1, stones, 1)
        
    def tryCross(self, step, stones, first):
        # this is to try based on the current status (step, stones)
        
        # 0. already in final
        if len(stones)==1:
            return True
        
        # 1. try step-1
        if first==0 and step-1>0:
            s=step-1
            if stones[0]+s in stones:
                new=stones.index(stones[0]+s)
                if self.tryCross(s,stones[new:],0):
                    return True
        
        # 2. try step
        s=step
        if stones[0]+s in stones:
            new=stones.index(stones[0]+s)
            if self.tryCross(s,stones[new:],0):
                return True
        
        # 3. try step+1
        s=step+1
        if first==0 and stones[0]+s in stones:
            new=stones.index(stones[0]+s)
            if self.tryCross(s,stones[new:],0):
                return True
        
        return False