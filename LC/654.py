# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def buildTree(n):
            if not n:
                return None
            m = max(n)
            i = n.index(m)
            res = TreeNode(m)
            res.left = buildTree(n[:i])
            res.right = buildTree(n[i+1:])
            return res
        return buildTree(nums)