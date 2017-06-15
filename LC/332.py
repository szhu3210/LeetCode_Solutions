class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def dfs(path, left):
            if left==0: return path
            destinations=sorted(d[path[-1]])
            for destination in destinations:
                d[path[-1]].remove(destination)
                path.append(destination)
                ret=dfs(path, left-1)
                if ret: return ret
                path.pop()
                d[path[-1]].append(destination)
        
        d=collections.defaultdict(list)
        for ticket in tickets:
            d[ticket[0]].append(ticket[1])
        res=['JFK']
        dfs(res, len(tickets))
        return res