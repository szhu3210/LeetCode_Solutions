class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        power=0
        for x in s[::-1]:
            res += (int(ord(str(x))-ord('A'))+1)*math.pow(26,power)
            power += 1
        return int(res)
        