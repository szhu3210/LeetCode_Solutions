from sets import Set
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        # Bit way, TLE
        # if len(num1)>len(num2):
        #     num1, num2 = num2, num1
        # num1, num2 = map(lambda x: int(x), list(num1)), map(lambda x: int(x), list(num2))
            
        # num1 = [0]*(len(num2)-len(num1)) + num1
        # while(Set(num2)!=Set([0])):
        #     for i in range(len(num1)):
        #         num1[i], num2[i] = (num1[i]+num2[i])%10, (num1[i]+num2[i])/10
        #     if num2[0]==1:
        #         num1.insert(0,0)
        #         num2.append(0)
        #     else:
        #         num2=num2[1:]+[0]
        # return ''.join(map(lambda x: str(x), num1))
        
        # Usual way
        if len(num1)>len(num2):
            num1, num2 = num2, num1
        num1, num2 = map(lambda x: int(x), list(num1)), map(lambda x: int(x), list(num2))
        num1 = [0]*(len(num2)-len(num1)) + num1
        num1.reverse()
        num2.reverse()
        
        c=0
        s=[]

        for x in xrange(len(num1)):
            s.append((num1[x]+num2[x]+c)%10)
            c=(num1[x]+num2[x]+c)/10
        if c>0:
            s.append(c)
        s.reverse()
        return ''.join([str(x) for x in s])