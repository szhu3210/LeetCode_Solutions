# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.dfs(s, t)
        
    def dfs(self, s, t):
        if self.isSame(s,t):
            return True
        if s and (self.dfs(s.left, t) or self.dfs(s.right, t)):
            return True
        return False
    
    def isSame(self, a, b):
        if a==b==None: return True
        if a==None or b==None: return False
        return a.val==b.val and self.isSame(a.left, b.left) and self.isSame(a.right, b.right)