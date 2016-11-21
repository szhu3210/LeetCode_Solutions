# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.f(root)[0]
        
    def f(self, root):
        if not root:
            return [True, 0]
        l=self.f(root.left)
        r=self.f(root.right)
        if l[0] and r[0] and abs(l[1]-r[1])<=1:
            return [True, max(l[1], r[1])+1]
        else:
            return [False, 0]