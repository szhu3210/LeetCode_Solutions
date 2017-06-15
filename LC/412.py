class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        d={(True,True): 'FizzBuzz', (True,False): 'Fizz', (False,True): 'Buzz'}
        for i in xrange(1,n+1):
            t=(i%3==0, i%5==0)
            res.append(d[t] if t in d else str(i))
        return res