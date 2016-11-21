# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.m=[]
        self.dfs(root)
        return max(self.m)
        
    def dfs(self, root):
        # return the biggest sum of path found in this root while secretly save its own local path to m
        if not root:
            return None
        l=self.dfs(root.left)
        r=self.dfs(root.right)
        l=(l if l and l>0 else 0)
        r=(r if r and r>0 else 0)
        res = max(l,r) + root.val
        # Here is the trick, the smart dfs secretly saves the local paths to global variable m
        self.m += [l+r+root.val]
        return res