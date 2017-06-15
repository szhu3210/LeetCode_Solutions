class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # build adjacency list using equations and values, {nominator: [(denominator, value), (), (), ... ]}
        graph = collections.defaultdict(list)
        for i in range(len(equations)):
            nominator, denominator = equations[i]
            value = values[i]
            graph[nominator].append((denominator, value))
            graph[denominator].append((nominator, 1/value))
        print graph
        
        # for each query, dfs from the start node to the end node. if cannot find, return -1.
        def dfs(s, d, value, path):
            if s not in graph:
                return -1.0
            if s in path:
                return -1.0
            path.add(s)
            if s==d:
                return value
            for dest, v in graph[s]:
                result = dfs(dest, d, value*v, path)
                if result!=-1:
                    # found value, return instantly
                    return result
                else:
                    # not found, keep searching
                    pass
            path.remove(s)
            return -1.0
                
        res=[]
        for source, destination in queries:
            res.append(dfs(source, destination, 1.0, set()))
        return res