class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        citations.append(0)
        if citations[0]>=l:
            return l
        else:
            i=0
        j=l
        while i<j-1:
            mid=(i+j)//2
            if citations[mid]>=l-mid:
                j=mid
            else:
                i=mid
        return l-j
        