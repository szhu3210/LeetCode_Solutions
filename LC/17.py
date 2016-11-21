class Solution(object):
    
    # dict for digits
    d = {
            '1':"*",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
            '0':" "
        }
    
    res=[]
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        
        
        ## iterative (O(n^3))
        res=[''] if digits else []
        for digit in digits:
            new=[]
            for a in res:
                for b in self.d[digit]:
                    new.append(a+b)
            res=new
        return res

    #     ## recursive (DFS)
    #     self.res=[]
    #     if not digits: return []
    #     self.dfs(digits, '')
    #     return self.res
        
    # def dfs(self, rest, str):
    #     if not rest:
    #         self.res.append(str)
    #         return
    #     for b in self.d[rest[0]]:
    #         nstr=str+b
    #         self.dfs(rest[1:], nstr)
