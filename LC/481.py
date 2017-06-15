class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [1,2,2]
        i = 1
        while len(t)<n:
            # extend t, using t[i:] numbers
            last = t[-1]
            new = []
            for j in t[i+1:]:
                new.extend([3-last]*j)
                last = 3 - last
            i = len(t)-1
            t.extend(new)
            # print new
            # print t
            # print i
        return t[:n].count(1)