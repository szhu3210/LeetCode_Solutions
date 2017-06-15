class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        
        ## greedy: count keeps the # of chars, valid keeps the leftmost valid index of a char.
        res=[]
        
        # count # of chars
        d=collections.defaultdict(int)
        for c in str:
            d[c]+=1
        
        # create a valid dict
        v=collections.defaultdict(int)
        
        # add char one by one, that with max # first, must have valid leftmost index
        for i in range(len(str)):
            c=None
            for key in d:
                if (not c or d[key]>d[c]) and d[key]>0 and v[key]<=i: # get c with max # and be valid
                    c=key
            if not c: return ''
            res.append(c)
            d[c]-=1
            v[c]=i+k
        return ''.join(res)