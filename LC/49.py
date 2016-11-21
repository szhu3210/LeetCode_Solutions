class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for x in strs:
            t=''.join(sorted(x))
            # return t
            if t in d:
                d[t].append(x)
            else:
                d[t]=[x]
        return [d[x] for x in d]