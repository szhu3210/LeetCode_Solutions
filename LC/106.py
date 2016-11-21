# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # use dict to make the search for index in inorder quicker
        inorder = {v:i for i, v in enumerate(inorder)}
        return self.helper(postorder, inorder, 0, len(postorder)-1, 0, len(inorder)-1)
        
    def helper(self, p, i, pl, pr, il, ir):
        res=None
        if pl<=pr and pr<len(p) and pl>=0:
            res=TreeNode(p[pr])
            ind=i[p[pr]]
            res.left= self.helper(p, i, pl, ind-il+pl-1, il, ind-1 )
            res.right=self.helper(p, i, ind-il+pl, pr-1, ind+1, ir )
        return res