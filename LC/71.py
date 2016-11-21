class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path=path.split('/')
        path=[x for x in path if x!='' and x!='.']
        res=[]
        for x in path:
            if x=='..':
                if res:
                    res.pop()
            else:
                res.append(x)
        return '/'+'/'.join(res)