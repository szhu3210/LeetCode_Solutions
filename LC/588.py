class FileSystem(object):

    def __init__(self):
        self.root = {'T': 'D'}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        cur = self.root
        p = path[1:].split('/')
        print p
        for e in p:
            if e:
                cur = cur[e]
        if cur['T']=='D':
            res = sorted(cur.keys())
            res.remove('T')
        else:
            res = [e]
        return res

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        cur = self.root
        for e in path[1:].split('/'):
            if e in cur:
                cur = cur[e]
            else:
                cur[e] = {'T': 'D'}
                cur = cur[e]
        print self.root

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        cur = self.root
        p = filePath[1:].split('/')
        for e in p:
            if e in cur:
                cur = cur[e]
            else:
                cur[e] = {'T': 'F'}
                cur = cur[e]
        if 'C' in cur:
            cur['C'] += content
        else:
            cur['C']=content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        cur = self.root
        print cur
        p = filePath[1:].split('/')
        for e in p:
            if e:
                cur = cur[e]
        cur['T']='F'
        if 'C' in cur:
            return cur['C']
        else:
            return ''


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)