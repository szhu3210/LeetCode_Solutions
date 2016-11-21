class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        counter={')':'(',']':'[','}':'{'}
        for x in s:
            if x in counter:
                if len(stack)>0 and counter[x]==stack[-1]:
                    stack.pop()
                    continue
            stack.append(x)
        return not stack