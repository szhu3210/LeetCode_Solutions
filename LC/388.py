class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res=0
        lines=input.split('\n')
        stack=[]
        for line in lines:
            name=line.lstrip('\t')
            level=len(line)-len(name)
            stack=stack[:level]
            stack.append(len(name))
            if '.' in name:
                res=max(res, sum(stack)+len(stack)-1)
        return res