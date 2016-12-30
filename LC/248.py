class Solution(object):
    # calculate number of stro. num.
    def findStroNum(self, n):
        if n==0:
            return 0
        if n==1:
            return 3
        if n==2:
            return 4
        if n==3:
            return 12
        return 5*self.findStroNum(n-2)
        
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        
        # check if input is valid
        if int(low)>int(high):
            return 0
            
        # reduce problem into fixed length
        if len(low)<len(high):
            full=len(low)*'9'
            full1='1'+'0'*(len(high)-1)
            return self.strobogrammaticInRange(low, full) + self.strobogrammaticInRange(full1, high) + sum([self.findStroNum(n) for n in range(len(low)+1, len(high))])
        
        # make strobogrammatic number in range
        n=len(low)
        
        # deal with 1-digit num. first since it may contain 0 (which is a special case)
        if n==1:
            return len([num for num in '018' if low<=num<=high])
        premid=[]
        
        # build stro. num. and keep checking if the num. is valid
        for i in range(n//2):
            if not premid:
                premid=[x for x in '1689' if low[0]<=x<=high[0]]
            else:
                premid=[x+y for x in premid for y in '01689' if low[:len(x)+1]<=x+y<=high[:len(x)+1]]
        
        # complete stro. num. and check if valid then return
        d={'0':'0','1':'1','6':'9','8':'8','9':'6'}
        if n%2:
            return len([num for num in [x+mid+''.join([d[y] for y in x[::-1]]) for x in premid for mid in '018'] if low<=num<=high])
        else:
            return len([num for num in [x+''.join([d[y] for y in x[::-1]]) for x in premid] if low<=num<=high])