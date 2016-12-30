class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.c(n+1)
        
    def c(self, n):
        if n<=10:
            return int(n>1)
        head=int(str(n)[0])
        tail=int(str(n)[1:] or 0)
        full=int('1'+'0'*(len(str(n))-1))
        if head==1 and tail==0:
            return 10*self.c(n/10)+(n/10)
        else:
            return (full if head>1 else 0) + head*self.c(full) + self.c(tail) + (tail)*(head==1)