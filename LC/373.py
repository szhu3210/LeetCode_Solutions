class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: return []
        l1, l2 = len(nums1), len(nums2)
        t = [(nums1[0]+nums2[0], 0, 0)]
        res=[]
        n=0
        while n<k and any(t):
            _, i, j = heapq.heappop(t)
            n+=1
            res.append([nums1[i],nums2[j]])
            if i+1<l1:
                heapq.heappush(t, (nums1[i+1]+nums2[j], i+1, j))
            if i==0 and j+1<l2:
                heapq.heappush(t, (nums1[i]+nums2[j+1], i, j+1))
        return res