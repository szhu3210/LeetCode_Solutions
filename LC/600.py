class Solution(object):
    def __init__(self):
        self.dp = {'': 1, '1': 2, '10': 3, '11': 3}

    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = "{0:b}".format(num).lstrip('0')
        if b in self.dp:
            return self.dp[b]
        s, e = b[:2], b[2:]
        if s=='10':
            res = self.findIntegers(int(e, 2)) + self.findIntegers(int('10' + len(e[1:])*'1', 2))
        else:
            res = self.findIntegers(int(len(e)*'1', 2)) + self.findIntegers(int('10' + len(e[1:])*'1', 2))
        self.dp[b] = res
        # print self.dp
        return res
