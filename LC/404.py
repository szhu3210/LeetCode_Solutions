# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# use a new function
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.find(root, False)
        
    def find(self, root, isLeft):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if isLeft else 0
        return self.find(root.left, True)+self.find(root.right,False)
        
# no use of a new function
# class Solution(object):
#     def sumOfLeftLeaves(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         sum=0
#         if not root:
#             return 0
#         if root.left and not root.left.left and not root.left.right:
#             sum+=root.left.val
#         sum+=self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
#         return sum