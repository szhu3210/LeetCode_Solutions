# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs([], root, res, s)
        return res
        
    def dfs(self, path, root, res, s):
        if not root:
            return
        if not root.left and not root.right:
            if sum(path)+root.val==s:
                res.append(path+[root.val])
            return
        self.dfs(path+[root.val], root.left, res, s)
        self.dfs(path+[root.val], root.right, res, s)
            