class Solution0(object):
    def __init__(self):
        self.mem={}
    
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            res=0
            if n not in self.mem:
                self.mem[n]=res
            return res
        if n%2==0:
            res = self.integerReplacement(n//2)+1
            if n not in self.mem:
                self.mem[n]=res
            return res
        res = min(self.integerReplacement(n-1),self.integerReplacement(n+1))+1
        if n not in self.mem:
            self.mem[n]=res
        return res
        
class Solution(object):
    def integerReplacement(self, n):
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn