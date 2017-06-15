class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = str(n)
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                t = list(num[i:])
                for j in range(len(t)-1, 0, -1):
                    if t[j]>t[0]:
                        first = t.pop(j)
                        rest = sorted(t)
                        res = int(num[:i] + first + ''.join(rest)) 
                        return res if res <= (2**31-1) else -1 
                print t
                raise ValueError('Error: cannot find bigger value!')
        return -1