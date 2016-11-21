# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessNum(1,n)
        
    def guessNum(self, i,j):
        if i==j:
            return i
        x=(i+j)/2
        y=guess(x)
        if y==0:
            return x
        elif y==1:
            return self.guessNum(x+1,j)
        else:
            return self.guessNum(i,x-1)
        
        