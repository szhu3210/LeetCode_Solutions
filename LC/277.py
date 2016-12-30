# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            flag=0 # assume the i-th person is potential celebrity
            for j in range(0,i)+range(i+1,n):
                if knows(i,j):
                    flag=1 # not celebrity
                    break
            if not flag:
                flag=0 # assume the guy is celebrity
                for j in range(0,i)+range(i+1,n):
                    if not knows(j,i):
                        flag=1 # not celebrity!
                        break
                if not flag: # celebrity found!
                    return i
        return -1