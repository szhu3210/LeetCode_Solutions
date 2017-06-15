class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def maxN(n,k,s):
            l=len(n)
            assert k<=l
            res=[]
            while k>0:
                a=n[s:l-k+1]
                m=max(a)
                res.append(m)
                s+=a.index(m)+1
                k-=1
            return res
    
        def merge(a, b):
            return [max(a,b).pop(0) for _ in a+b]
        
        return max([merge(maxN(nums1, i, 0), maxN(nums2, k-i, 0)) for i in range(k+1) if i<=len(nums1) and k-i<=len(nums2)])
    
