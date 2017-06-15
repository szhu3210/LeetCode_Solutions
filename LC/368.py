class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={-1:set()} # use d to store the valid set ending in key, -1 is for default value 0.
        for n in sorted(nums): # need to find the longest set that is valid
            longest_key = -1 # default key
            for key in d:
                if n % key == 0 and len(d[key]) > len(d[longest_key]): # valid longer set found
                    longest_key = key
            d[n] = d[longest_key] | set([n])
        # print d
        return list(d[max(d, key = lambda x: len(d[x]))])