class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l=len(num)
        for i in range(l//2):
            if num[i]=='6':
                if num[l-1-i]!='9':
                    return False
            elif num[i]=='9':
                if num[l-1-i]!='6':
                    return False
            elif num[i] in ('0','1','8'):
                if num[l-1-i]!=num[i]:
                    return False
            else:
                return False
        return (num[l//2] in ('0','1','8')) if l%2==1 else True