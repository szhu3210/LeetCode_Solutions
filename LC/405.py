class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # cheat
        # return hex((num + (1 << 32)) % (1 << 32))[2:]
        
        # regular
        if num==0: return '0'
        res=''
        map='0123456789abcdef'
        for x in range(8):
            res=(map[num&15])+res
            num=num>>4
        return res.lstrip('0')