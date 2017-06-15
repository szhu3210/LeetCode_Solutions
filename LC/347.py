class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d=collections.defaultdict(int)
        for num in nums:
            d[num]+=1
        return [_[1] for _ in sorted([(d[key],key) for key in d],reverse=True)[:k]]