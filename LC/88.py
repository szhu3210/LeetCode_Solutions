class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums2[:n]+nums1[:m]
        k=0
        i=n
        j=0
        while(i<m+n and j<n):
            if nums1[i]<=nums2[j]:
                nums1[k]=nums1[i]
                i+=1
                k+=1
            else:
                nums1[k]=nums2[j]
                j+=1
                k+=1
        if i==m+n:
            nums1[k:]=nums2[j:]