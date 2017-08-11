class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>len(t):
            return False
        
        d = collections.defaultdict(list)
        for i,c in enumerate(t):
            d[c].append(i)
        # print d
        
        cur = 0 # current index in s, greedy
        for c in s:
            if d[c]:
                index = bisect.bisect_left(d[c], cur)
                # print index
                if index==len(d[c]):
                    return False
                cur = d[c][index]+1
            else:
                # print c
                return False
        return True