class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        # deal with negative nums
        sign='-' if (numerator*denominator<0) else ''
        numerator=abs(numerator)
        denominator=abs(denominator)
        
        # t records the result and r records the remainder
        t=[]
        r=[]
        
        # calculate remainder until it's 0 or in r then return
        while 1:
            t.append(numerator//denominator)
            r.append(numerator%denominator)
            if r[-1]==0:
                return sign+str(t[0])+('.'+''.join(map(lambda x: str(x),t[1:])) if t[1:] else '')
            if r[-1] in r[:-1]:
                return sign+str(t[0])+'.'+''.join(map(lambda x: str(x),t[1:r.index(r[-1])+1]))+'('+''.join(map(lambda x: str(x),t[r.index(r[-1])+1:]))+')'
            numerator=r[-1]*10