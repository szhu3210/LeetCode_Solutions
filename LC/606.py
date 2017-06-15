# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        res = str(t.val)
        if t.right:
            res += '('+ self.tree2str(t.left) +')' + '('+ self.tree2str(t.right) +')'
            return res
        if t.left:
            res += '('+ self.tree2str(t.left) +')'
            return res
        return res