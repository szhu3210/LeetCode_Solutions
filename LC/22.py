class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def draw(cur, n, m, r):
            if n==0 and m==0:
                res.append(cur)
            if n==0 and m>0:
                draw(cur+')', n, m-1, r-1)
            if n>0 and m>0:
                draw(cur+'(', n-1, m, r+1)
                if r>0:
                    draw(cur+')', n, m-1, r-1)
        
        res=[]
        draw('', n, n, 0)
        return res
