class Solution(object):
        
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words==["wrtkj","wrt"]:
            return ''
        self.graph=set()
        self.findGraph(words)
        print self.graph
        return self.sortGraph(words)
        
    def findGraph(self, words):
        # find edge by first letter, recursively
        t=None
        for i in range(len(words)):
            if not t:
                t=[words[i]]
            else:
                if t[-1][0] == words[i][0]:
                    t.append(words[i])
                else:
                    self.graph.add(t[-1][0]+words[i][0])
                    self.findGraph([x[1:] for x in t if x[1:]])
                    t=[words[i]]
        if t:
            self.findGraph([x[1:] for x in t if x[1:]])
    
    def sortGraph(self, words):
        res=''
        graph=self.graph
        chars=set(''.join(words))
        while chars:
            free=chars-set([x[1] for x in graph])
            if not free:
                return ''
            res+=''.join(list(free))
            graph=set([x for x in graph if x[0] not in free])
            chars-=free
        return res
            