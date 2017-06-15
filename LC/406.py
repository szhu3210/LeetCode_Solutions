class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        q=sorted(people, key=lambda x: -x[0]+x[1]/10000.0)
        for h,i in q:
            res.insert(i,[h,i])
        return res