class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # find abs values and sign
        a=abs(dividend)
        b=abs(divisor)
        signa=False if dividend<0 else True
        signb=False if divisor<0 else True
        nsign=(signa and not signb) or (signb and not signa)
        
        # find maximum length of binary number of result
        p=[]
        x=b
        while x<=a:
            p.append(x)
            x+=x
        x=0
        res=[0]*len(p)
        for i in xrange(len(p)-1,-1,-1):
            if p[i]+x<=a:
                x+=p[i]
                res[i]=1
        
        # cal result
        n=1
        r=0
        for i in xrange(len(res)):
            r+=n*res[i]
            n+=n
            
        # get result
        r = -r if nsign else r
        if r>=2147483648 or r<-2147483648:
            return 2147483647
        else:
            return r