class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        temp = []
        res = {}
        for x in range(ord('a'), ord('a') + 26):
            res[chr(x)] = 0
        i = 0
        j = 0
        while j + 1 < len(p):
            if ord(p[j + 1]) - ord(p[j]) == 1 or (p[j + 1] == 'a' and p[j] == 'z'):
                j += 1
            else:
                temp.append(p[i:j + 1])
                i = j = j + 1
        temp.append(p[i:j + 1])

        for t in temp:
            for i,x in enumerate(t):
                res[x]=max(res[x], i+1)
        print res
        return sum([res[key] for key in res])
