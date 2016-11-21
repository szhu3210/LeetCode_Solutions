class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # count
        # return [chr(x) for x in range(97,123) if s.count(chr(x))!=t.count(chr(x))][0]
        
        # hash table
        # ds={}
        # dt={}
        # for x in range(97,123):
        #     ds[chr(x)]=s.count(chr(x))
        #     dt[chr(x)]=t.count(chr(x))
        # for x in range(97,123):
        #     if ds[chr(x)]!=dt[chr(x)]:
        #         return chr(x)

        # bit manipulation
        a=0
        for x in s+t:
            a^=ord(x)
        return chr(a)