class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        ## my solution
        # res=''
        # for i in xrange(len(bin(m))-2):
        #     if m>>i & 1 == 0:
        #         res='0'+res
        #     elif (((m>>i) + 1) << i) <= n:
        #         res='0'+res
        #     else:
        #         res='1'+res
        # return int(res,2)
        
        ## quick solution
        c=0
        for i in xrange(len(bin(m))-2):
            if m>>i != n>>i:
                c+=1
            else:
                break
        return m>>c<<c