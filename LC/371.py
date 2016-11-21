class Solution(object):
    
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    # 32 bits interger min
    MIN = 0x80000000
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # recursive using simulated Int32
        # if b==0:
        #     return a if a<self.MAX else ~(a ^ self.mask)
        # return self.getSum((a ^ b) & self.mask, (a & b) << 1 & self.mask)
        
        # iterative
        for _ in xrange(32):
            a, b = (a ^ b), (a & b) << 1
        return a if a&self.MIN else a&self.mask 