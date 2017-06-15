class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1
        visited = set() # visited nodes

        # iterate from 0 to N-1
        for n in range(len(nums)):
            if n in visited:
                continue
            visited.add(n)
            size = 1
            c = n
            while nums[c]!=n: # not reach the loop
                c = nums[c]
                visited.add(c)
                size += 1
                # print 'new c: %d' % c
            if size > len(nums)//2:
                return size
            res = max(res, size)
            # print visited
        return res