# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # iterative
        # res = 0
        # nodes = [root] if root else []
        # while(nodes):
        #     res += 1
        #     new = []
            
        #     ## iterative and fast version
        #     for j in nodes:
        #         if not j.left and not j.right:
        #             return res
        #         new.extend([j.left, j.right])
        #     nodes=filter(None, new)
            
        #     # ## Pythonic but slow version
        #     # if (None, None) in [(j.left, j.right) for j in nodes]:
        #     #     return res
        #     # nodes=filter(None, [i for j in nodes for i in [j.left, j.right]])
            
        # return res
        
        # recursive
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)
        