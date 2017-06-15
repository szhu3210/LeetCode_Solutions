# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.longest(root)
        return self.res
        
    def longest(self, root):
        if not root:
            return (0,0)
        lu, ld = self.longest(root.left)
        ru, rd = self.longest(root.right)
        
        up = max(\
                lu + 1 if (root.left and root.val == root.left.val + 1) else 1,\
                ru + 1 if (root.right and root.val == root.right.val + 1) else 1,\
                )
        
        down = max(\
                ld + 1 if (root.left and root.val == root.left.val -1) else 1,\
                rd + 1 if (root.right and root.val == root.right.val -1) else 1,\
                )
                
        if root.left and root.right:
            if (root.left.val + 1 == root.val == root.right.val - 1):
                self.res = max(self.res, lu+rd+1)
            if (root.left.val - 1 == root.val == root.right.val + 1):
                self.res = max(self.res, ru+ld+1)
        
        self.res = max(self.res, up, down)
        
        return up, down
        