class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def subStr(a, b):
            b = iter(b)
            return all(c in b for c in a)
        d = map(lambda y: y[1], sorted(map(lambda x: (-len(x), x), d)))
        # print d
        for w in d:
            if subStr(w, s):
                return w
        return ''