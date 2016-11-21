class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        # normal solution
        p=nums[0]
        if target==p:
            return True
        i=0
        j=len(nums)-1
        while i<len(nums) and nums[i]==p:
            i+=1
        while j>=0 and nums[j]==p:
            j-=1
        if target>p:
            while(i<=j):
                m=(i+j)/2
                if nums[m]<p:
                    j=m-1
                    continue
                if nums[m]==target:
                    return True
                if nums[m]<target:
                    i=m+1
                else:
                    j=m-1
        else:
            while(i<=j):
                m=(i+j)/2
                if nums[m]>=p:
                    i=m+1
                    continue
                if nums[m]==target:
                    return True
                if nums[m]<target:
                    i=m+1
                else:
                    j=m-1
        # return i,j
        return False