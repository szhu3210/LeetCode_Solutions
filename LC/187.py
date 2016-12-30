class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d=set([])
        res=set([])
        for i in range(len(s)-9):
            t=s[i:i+10]
            if t in d:
                if t not in res:
                    res.add(t)
            else:
                d.add(t)
        return list(res)