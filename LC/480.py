class Solution(object):
    def medianSlidingWindow(self, nums, k):
        medians, window = [], []
    
        for i in xrange(len(nums)):
    
            # Find position where outgoing element should be removed from
            if i >= k:
              # window.remove(nums[i-k])        # this works too
              window.pop(bisect.bisect(window, nums[i - k]) - 1)
    
            # Maintain the sorted invariant while inserting incoming element
            bisect.insort(window, nums[i])
    
            # Find the medians
            if i >= k - 1:
              medians.append(float((window[k / 2]
                if k & 1 > 0
                else(window[k / 2 - 1] + window[k / 2]) * 0.5)))
    
        return medians