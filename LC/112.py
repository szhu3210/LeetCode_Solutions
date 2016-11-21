# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if (not root): return False
        r = sum - root.val
        if not root.left and not root.right: return r == 0
        return self.hasPathSum(root.left, r) or self.hasPathSum(root.right, r) # not arrive leaf or arrived leaf but wrong answer