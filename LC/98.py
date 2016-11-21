# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        l = self.dfs(root)
        return all(l[i] < l[i+1] for i in xrange(len(l)-1))
    
    def dfs(self, root):
        return self.dfs(root.left) + [root.val] + self.dfs(root.right) if root else []