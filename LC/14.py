class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs,key=len)
        for x,c in enumerate(shortest):
            for y in strs:
                if y[x] != c:
                    return shortest[:x]
        return shortest