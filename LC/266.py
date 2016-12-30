class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d=collections.defaultdict(int)
        for c in s:
            d[c]+=1
        t=0
        for c in d:
            if d[c]%2==1:
                if t==0:
                    t=1
                else:
                    return False
        return True