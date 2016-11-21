class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) < len(t): return ''
        # use dict and list w/ optimization
        i = 0
        j = 0
        d = {}
        lenT = len(t)
        for x in t:
            d[x] = d.get(x, 0) + 1
        t = {}
        l = []
        minLen = None
        minStr = None
        missing = lenT
        while j < len(s):
            if s[j] in d:
                l.append((j, s[j]))
                t[s[j]] = t.get(s[j], 0) + 1
                missing -= t[s[j]] <= d[s[j]]
                if missing > 0:
                    j+=1
                    continue
                while t[l[0][1]] > d[l[0][1]]:
                    t[l[0][1]] -= 1
                    l.pop(0)
                i = l[0][0]
                length = j - i + 1
                if length < minLen or not minLen:
                    minLen = length
                    minStr = (i, j)
            j += 1
        return s[minStr[0]:minStr[1] + 1] if minStr else ''

