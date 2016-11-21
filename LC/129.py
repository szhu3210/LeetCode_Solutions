# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        ## dfs + stack
        stack=[root.val, root]
        res=0
        while stack:
            s, node = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += s*10+node.val
                if node.left:
                    stack.append(s*10+node.val, node.left)
                if node.right:
                    stack.append(s*10+node.val, node.right)
        return res
        
        ## recursive dfs
        self.res=0
        self.dfs(0, root)
        return self.res
        
    def dfs(self, s, root):
        if not root:
            return
        if not root.left and not root.right:
            self.res += root.val+s*10
        if root.left:
            self.dfs(s*10+root.val, root.left)
        if root.right:
            self.dfs(s*10+root.val, root.right)
        