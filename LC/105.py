# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # use dict to make the search for index in inorder quicker
        inorder = {v:i for i, v in enumerate(inorder)}
        return self.helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
        
    def helper(self, p, i, pl, pr, il, ir):
        res=None
        if pl<=pr and pr<len(p) and ir<len(i):
            res=TreeNode(p[pl])
            ind=i[p[pl]]
            res.left= self.helper(p, i, pl+1, pl+ind-il, il, ind-1 )
            res.right=self.helper(p, i, pl+ind-il+1, pr, ind+1, ir )
        return res