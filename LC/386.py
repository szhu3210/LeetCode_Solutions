class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # short but TLE
        # return map(int, sorted(map(str, range(1, n+1))))
    
        # buckle sort like (?)
        # pass
        
        # start from 1 then check if the next number exceeds n
        self.res = []
        self.gen(n, 0, nozero=True)
        return self.res
        
    def gen(self, n, lead, nozero=False):
        for i in range(int(nozero), 10):
            new = lead*10+i
            if new <= n:
                self.res.append(new)
                if new*10<=n:
                    self.gen(n, new)