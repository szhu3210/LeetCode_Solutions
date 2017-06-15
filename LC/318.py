class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d=collections.defaultdict(int)
        for w in words:
            mask=0
            for c in set(w):
                mask |= 1 << (ord(c)-97)
            d[mask]=max(d[mask],len(w))
        return max([d[i]*d[j] for i in d for j in d if i&j==0] or [0])