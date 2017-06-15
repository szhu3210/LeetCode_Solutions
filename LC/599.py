import collections
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # make dict for both list
        d1 = {}
        for i, r in enumerate(list1):
            d1[r] = i
        d2 = {}
        for i, r in enumerate(list2):
            d2[r] = i
        # print d1, d2

        # find common list
        common = list(set(list1) & set(list2))
        # print common

        # calculate index sum and store in a dict
        d = collections.defaultdict(list)
        for r in common:
            d[(d1[r]+d2[r])].append(r)
        # print d

        # output the minimum index sum ones
        res = d[min(d.keys())]
        # print res
        return res