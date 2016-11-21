class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        ## iterative (DP) (35ms)
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        co=[(-1,-1)]
        x=0
        while x<l3 and co:
            nco=[]
            for c in co:
                if c[0]<l1-1 and s3[x]==s1[c[0]+1] and (c[0]+1,c[1]) not in nco:
                    nco.append((c[0]+1,c[1]))
                if c[1]<l2-1 and s3[x]==s2[c[1]+1] and (c[0],c[1]+1) not in nco:
                    nco.append((c[0],c[1]+1))
            co=nco
            x+=1
        return (l1-1,l2-1) in co
        
        ## recursive (keep historical record) (68ms)
    #     d={}
    #     return self.helper(s1,s2,s3,d)
    
    # def helper(self, s1,s2,s3,d):
    #     if len(s1)+len(s2)!=len(s3):
    #         return False
    #     if (s1,s2,s3) in d:
    #         return False
    #     if s1=='':
    #         t = s2==s3
    #         if t:
    #             return True
    #         else:
    #             d[(s1,s2,s3)]=t
    #             return False
    #     if s2=='':
    #         t = s1==s3
    #         if t:
    #             return True
    #         else:
    #             d[(s1,s2,s3)]=t
    #             return False
    #     t1 = self.helper(s1[1:],s2,s3[1:],d) if s3[0]==s1[0] else False
    #     if t1:
    #         return True
    #     t2 = self.helper(s1,s2[1:],s3[1:],d) if s3[0]==s2[0] else False
    #     if t2:
    #         return True
    #     d[(s1,s2,s3)]=False
    #     return False