# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # # iterative
        # nodes=[root] if root else []
        # res=0
        # while(nodes):
        #     nodes=filter(None,[i for j in nodes for i in [j.left, j.right]])
        #     res+=1
        # return res
        
        # # recursive
        # if root==None:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right))+1