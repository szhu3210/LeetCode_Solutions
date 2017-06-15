class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        s=0
        p=preorder.split(',')
        i=0
        while i<len(p):
            if p[i]=='#':
                s-=1
            else:
                s+=1
            if s<0:
                break
            i+=1
        # return s,i
        return s==-1 and i==len(p)-1