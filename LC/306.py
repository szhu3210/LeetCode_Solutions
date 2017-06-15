class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l=len(num)
        for i in range(l//2):
            for j in range(i+1, (i+1+l)//2):
                first=num[:i+1]
                second=num[i+1:j+1]
                rest=num[j+1:]
                if rest and self.check(first, second, rest):
                    return True
        return False
        
    def check(self, first, second, rest):
        print first, second, rest
        if not rest:
            return True
        if any([str(int(a))!=a for a in (first, second)]):
            return False
        result=str(int(first)+int(second))
        l=len(result)
        if rest.startswith(result):
            return self.check(second, result, rest[l:])
        else:
            return False