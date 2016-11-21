class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is just a greedy algorithm
        # i records the current position
        i=0
        # res is the step counter
        res=0
        # we need to jump if we have not reached the end
        while i<len(nums)-1:
            # if the range covers the end position we can return
            if nums[i]+i>=len(nums)-1:
                return res+1
            # we need to evaluate how many steps we jump by calculating the maximum possible range
            t=0 # stores the maximum range
            step=0 # stores the step we are going to jump
            for x in range(1, nums[i]+1): # loop through the range
                a = nums[i+x]-(nums[i]-x) # calculate the maximum range if jump by distance x
                if a > t:  # find the maximum and record the optimum step
                    t = a
                    step = x
            # okay, let's jump and count
            i+=step
            res+=1
        return res