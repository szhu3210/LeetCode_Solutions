class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        ## 49ms Solution.
        def dfs(nums, start, end, cache):
            if (start, end) not in cache:
                cache[(start,end)] = nums[start] if start == end else max(nums[start]-dfs(nums, start+1, end, cache), nums[end]-dfs(nums, start, end-1, cache))
            return cache[(start, end)]
        return dfs(nums, 0, len(nums)-1, {})>=0
        
        ## My solution.
        self.nums = nums
        return self.win(1, 0, 0, len(nums)-1)
        
    def win(self, player, adv, i, j):
        # i, j indicates the border of current nums (save mem.)
        # player indicates current player
        # adv indicate current player's advantage to the counterpart
        if i==j:
            dif = adv + self.nums[i]
            if player==1:
                res = dif>=0
            else:
                res = dif<=0
            # print player, adv, self.nums[i], dif, res
            return res
        else:
            # player can choose either start or end
            # if choose start
            adv1 = adv + self.nums[i]
            res1 = self.win(3-player, -adv1, i+1, j) # counter part will have -adv1 advantage
            if player==1 and res1:
                return res1
            if player==2 and not res1:
                return res1
            adv2 = adv + self.nums[j]
            res2 = self.win(3-player, -adv2, i, j-1) 
            if player==1:
                res = res1 or res2 # either works for P1, it works
                # print player, adv, self.nums[i:j+1], res
                return res
            else:
                res = res1 and res2 # if no matter what P2's choice is, P1 must win
                # print player, adv, self.nums[i:j+1], res
                return res