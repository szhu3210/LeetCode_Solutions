# class Solution(object):
#     # slow version
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         res='0'
#         for i,y in enumerate(num2[::-1]):
#             b=self.multiplyDigit(num1, y)
#             a=b+'0'*i if b!='0' else '0' 
#             res=self.addStrings(res, a)
#         return res
#     def multiplyDigit(self, X, Y):
#         rX=X[::-1]
#         y=ord(Y)-ord('0')
#         if y==0 or X=='0': return '0'
#         if y==1: return X
#         c=0
#         resR=''
#         for x in rX:
#             n=ord(x)-ord('0')
#             t=(n*y%10+c)%10
#             c=(n*y%10+c)/10+n*y/10
#             resR+=chr(t+ord('0'))
#         resR+=chr(c+ord('0')) if c>0 else''
#         return resR[::-1]
#     def addStrings(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         if len(num1)>len(num2):
#             num1, num2 = num2, num1
#         num1, num2 = map(lambda x: int(x), list(num1)), map(lambda x: int(x), list(num2))
#         num1 = [0]*(len(num2)-len(num1)) + num1
#         num1.reverse()
#         num2.reverse()
#         c=0
#         s=[]
#         for x in xrange(len(num1)):
#             s.append((num1[x]+num2[x]+c)%10)
#             c=(num1[x]+num2[x]+c)/10
#         if c>0:
#             s.append(c)
#         s.reverse()
#         return ''.join([str(x) for x in s])

# fast version
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res=[0]*(len(num1)+len(num2))
        for i,x in enumerate(num1[::-1]):
            for j,y in enumerate(num2[::-1]):
                res[i+j]+=(ord(x)-48)*(ord(y)-48)
        for i in xrange(len(res)-1):
            res[i+1]+=res[i]/10
            res[i]=res[i]%10
        res= ''.join([chr(x+48) for x in res[::-1]]).lstrip('0')
        return res if res else '0'
