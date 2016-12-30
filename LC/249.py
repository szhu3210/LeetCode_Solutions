class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d=collections.defaultdict(list)
        for s in strings:
            d[tuple([((ord(s[i])-ord(s[0]))%26) for i in range(len(s))])].append(s)
        return [d[key] for key in d]