class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        for i in range(k):
            #remove prefixed 0
            while(num[0]=='0' if num else 0):
                num=num[1:]
                
            #remove 1 digit
            if len(num)>1:
                if num[1]=='0':
                    num=num[2:]
                    continue
            m=0
            d=-1
            for i,c in enumerate(num):
                if int(c)>=m:
                    m=int(c)
                else:
                    d=i-1
                    break
            num=num[:d]+(num[d+1:] if d>-1 else '')
        return num if num else '0'