class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = lo = 0
        c = collections.Counter()
        hi = -1
        for hi in range(len(s)):
            c[s[hi]] += 1
            n = c.most_common(1)[0][1]
            if hi-lo+1-n > k:
                c[s[lo]] -= 1
                lo += 1
        return hi-lo+1