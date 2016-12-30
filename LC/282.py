class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(num, target, None, '', res)
        return sorted(res)
        
    def dfs(self, num, target, pre, path, res):
        if not num: return
        if (num=='0' or (num[0]!='0')) and (int(num)==target if pre==None else int(num)*pre==target):
                res.append(path+num)
        else:
            for i in range(1, len(num)):
                left=num[:i]
                right=num[i:]
                if left!='0' and left[0]=='0': # leading '0' but not '0' => invalid number
                    pass
                else:
                    # left is a valid number
                    leftVal=pre*int(left) if pre!=None else int(left)
                    # +
                    self.dfs(right, target-leftVal, None, path+left+'+', res)
                    # -
                    self.dfs(right, target-leftVal, -1, path+left+'-', res)
                    # *
                    self.dfs(right, target, leftVal, path+left+'*', res)