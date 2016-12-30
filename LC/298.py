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
        self.res=0
        self.dfs(root, None, 0)
        return self.res
    
    def dfs(self, node, last, length):
        if not node:
            self.res=max(self.res, length)
            return
        if last!=None and node.val==last+1:
            self.dfs(node.left, node.val, length+1)
            self.dfs(node.right, node.val, length+1)
        else:
            self.res=max(self.res, length)
            self.dfs(node.left, node.val, 1)
            self.dfs(node.right, node.val, 1)