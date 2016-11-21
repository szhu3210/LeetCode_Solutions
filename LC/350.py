class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums2:
            if x in nums1:
                res.append(x)
                nums1.remove(x)
        return res
        