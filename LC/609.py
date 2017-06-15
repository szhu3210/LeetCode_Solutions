class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for path in paths:
            l = path.split()
            directory = l[0]
            for file in l[1:]:
                name, content = file.split('(')
                content = content[:-1]
                d[content].append(directory+'/'+name)
        # print d
        res = []
        for key in d:
            if len(d[key])>1:
                res.append(d[key])
        return res