class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        
        l = [[-d[key],key] for key in d]
        l.sort()
        # print l
        
        res = ''.join([(-n)*c for n,c in l])
        
        return res