class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # ## normal way
        # res=0
        
        # # From left to right assuming there exists a higher or same level. Keep the water in temp until we verify that.
        # t=0
        # i=0
        # j=0
        # while j<len(height):
        #     if height[j]<height[i]:
        #         t+=height[i]-height[j]
        #     else:
        #         res+=t
        #         t=0
        #         i=j
        #     j+=1
            
        # # Now i indicates the highest bar. We inverse the remaining part of the bars and do the same thing.
        # height=height[i:][::-1]
        # t=0
        # i=0
        # j=0
        # while j<len(height):
        #     if height[j]<height[i]:
        #         t+=height[i]-height[j]
        #     else:
        #         res+=t
        #         t=0
        #         i=j
        #     j+=1
            
        # return res
        
        ## another way
        if not height:
            return 0
        i=0
        j=len(height)-1
        
        # between i and j, we can trap min(height[i],height[j])*(j-i+1) of water. Then we remove the brick of the lower one and meanwhile decrease the volume of water by lower, until we find a higher brick. Then the trapped water could increase by (min(height[i],height[j])-lower)*(j-i+1). Update lower, and repeat until i>j.
        res=0
        lower=0
        while i<=j:
            h=min(height[i],height[j])
            if h>lower:
                lower=h
            if height[i]<=height[j]:
                res+=lower-height[i]
                i+=1
            else:
                res+=lower-height[j]
                j-=1 
        return res
            