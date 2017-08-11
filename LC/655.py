# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def expand(a, ah, al, sh, sl):
            # print 'before expand'
            # print a
            if not a:
                a = [['']*sl]*sh
            else:
                t = sh-ah
                for level in range(t):
                    for i in range(len(a)):
                        # each line insert between columns
                        t = ['']
                        for x in a[i]:
                            t.append(x)
                            t.append('')
                        a[i] = t
                a.extend([['']*sl]*(sh-ah))
            # print 'after expand'
            # print a
            return a
            
        def draw(root):
            if not root:
                return None, 0, 0
            l, lh, ll = draw(root.left)
            r, rh, rl = draw(root.right)
            
            if not l and not r:
                return [[str(root.val)]], 1, 1
            
            sh = max(lh, rh)
            sl = max(ll, rl)
                        
            if lh<sh:
                l = expand(l, lh, ll, sh, sl)
            else:
                r = expand(r, rh, rl, sh, sl)
                
            # print l, r
            
            res = []
            res.append(['']*sl + [str(root.val)] + ['']*sl)
            for i in range(len(l)):
                res.append(l[i] + [''] + r[i])
            return res, sh+1, sl*2+1
            
        res, _1, _2 = draw(root)
        # for line in res:
        #     print line
        return res