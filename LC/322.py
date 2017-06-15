class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ## DP bottom-up (faster, O(n*amount) time, O(n) space)
        coins.sort()
        f=[-1]*(amount+1)
        f[0]=0
        for i in range(1,amount+1):
            t=None
            for j in coins:
                if i>=j:
                    if f[i-j]>=0:
                        t=min(t,f[i-j]) if t!=None else f[i-j]
                else:
                    break
            f[i]=t+1 if t!=None else -1
        return f[-1]
        
        ## DP top-down (O(n*amount) time, O(amount) space)
    #     self.mem=[-2]*(amount+1)
    #     self.mem[0]=0
    #     return self.helper(sorted(coins), amount)
    
    # def helper(self, coins, amount):
    #     temp=[]
    #     if self.mem[amount]!=-2: return self.mem[amount]
    #     for coin in coins:
    #         if amount>=coin:
    #             t=self.helper(coins, amount-coin)
    #             if t>=0:
    #                 temp.append(t+1)
    #         else:
    #             break
    #     if temp:
    #         res=min(temp)
    #         del temp
    #         self.mem[amount]=res
    #         return res
    #     self.mem[amount]=-1
    #     return -1