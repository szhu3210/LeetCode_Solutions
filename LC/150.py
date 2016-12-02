class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for token in tokens:
            if token in set(['+','-','*','/']):
                b=stack.pop()
                a=stack.pop()
                if token == '+':
                    stack.append(int(a)+int(b))
                if token == '-':
                    stack.append(int(a)-int(b))
                if token == '*':
                    stack.append(int(a)*int(b))
                if token == '/':
                    stack.append(int(a)/float(b))
            else:
                stack.append(token)
        return int(stack[0])
                