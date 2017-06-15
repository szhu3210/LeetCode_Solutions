class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## DP iterative (bottom-up)
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]
    
        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                           nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
            
        ## DP recursive (top-down)
        # nums = [1] + nums + [1]
        # n = len(nums)
        # dp = [[0] * n for _ in xrange(n)]

        # def calculate(i, j):
        #     if dp[i][j] or j == i + 1: # in memory or gap < 2
        #         return dp[i][j]
        #     coins = 0
        #     for k in xrange(i+1, j): # find the last balloon
        #         coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
        #     dp[i][j] = coins
        #     return coins

        # return calculate(0, n-1)