class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        # bfs from left to right to check invalid ')'
        bfs = set([(s, 0)])  # s is the result and [1] is the index before which is valid
        while bfs:
            bfs_new = set()
            for s, ind in bfs:
                c = 0  # counter to check if s is valid
                for i in range(ind, len(s)):
                    c += 1 if s[i] == '(' else -1 if s[i] == ')' else 0
                    if c < 0:  # invalid index found
                        j = i  # scan from i to 0 and delete each different ')'
                        flag = 0  # check if a block of continuous ')' has ever been deleted
                        # delete ')'
                        while j >= 0:
                            if s[j] == ')':
                                bfs_new.add((s[:j] + s[j + 1:], i))
                            j -= 1
                        break
                if c >= 0:
                    res.append(s)
            bfs = bfs_new

        # bfs from right to left to check invalid '('
        bfs = set([(x, len(x)-1) for x in res])  # s is the result and [1] is the index after which is valid
        res=[]
        while bfs:
            bfs_new = set()
            for s, ind in bfs:
                c = 0  # counter to check if s is valid
                for i in range(ind, -1, -1):
                    c += 1 if s[i] == ')' else -1 if s[i] == '(' else 0
                    if c < 0:  # invalid index found
                        j = i  # scan from i to len(s)-1 and delete each different '('
                        flag = 0  # check if a block of continuous '(' has ever been deleted
                        # delete '('
                        while j <= len(s)-1:
                            if s[j] == '(':
                                bfs_new.add((s[:j] + s[j + 1:], i-1))
                            j += 1
                        break
                if c == 0:
                    res.append(s)
            bfs = bfs_new

        return res