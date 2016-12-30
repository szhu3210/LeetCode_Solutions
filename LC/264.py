class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2,i3,i5=0,0,0
        nums=[1]
        for _ in xrange(n-1):
            u2,u3,u5=nums[i2]*2,nums[i3]*3,nums[i5]*5
            nums.append(min(u2,u3,u5))
            if u2==nums[-1]:
                i2+=1
            if u3==nums[-1]:
                i3+=1
            if u5==nums[-1]:
                i5+=1
        return nums[-1]
            