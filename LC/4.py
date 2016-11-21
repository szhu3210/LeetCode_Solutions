class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # find the median
        A = nums1
        B = nums2
        if (len(nums1) + len(nums2))%2 == 1:
            return self.kth(A, B, (len(nums1) + len(nums2)) // 2)
        else:
            return (self.kth(A, B, (len(nums1) + len(nums2)) // 2) + self.kth(A, B, (len(nums1) + len(nums2)) // 2 -1)) / 2.0     

        
    # find kth element in two ordered lists
    def kth(self, a, b, k):
        
        # if reduced to only one list
        if not a:
            return b[k]
        if not b:
            return a[k]
            
        ## reduce the list
        
        # find the "median" of a and b
        ia = len(a) // 2
        ib = len(b) // 2
        ma = a[ia]
        mb = b[ib]
        
        ## check if kth element is in one half of both lists
        
        # k is in the second half of both lists
        if ia + ib < k:
            # ma is less than mb so that we can reduce part of mb list
            if ma < mb:
                return self.kth(a[ia+1:], b, k-ia-1)
            else:
                return self.kth(a, b[ib+1:], k-ib-1)
        # k is in the first half of both lists
        else:
            # ma is larger than mb so that we can reduce part of ma list
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
        
        
        
           
        
            
                
                
                
                
                
                
                
                
                
                
                