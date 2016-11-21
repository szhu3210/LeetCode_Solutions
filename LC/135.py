class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ## greedy
        candy=[1 for _ in range(len(ratings))]
        for i in range(len(ratings))[1:]:
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)
        return sum(candy)
        