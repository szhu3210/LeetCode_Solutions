# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        ## concise way
        if not root:
            return
        self.flatten(root.right)
        if not root.left:
            return
        self.flatten(root.left)
        temp=root.left
        while temp.right:
            temp=temp.right
        temp.right=root.right
        root.right=root.left
        root.left=None
        
        ## morris traversal
        # cur=root
        # while cur:
        #     if cur.left:
        #         temp=cur.left
        #         while temp.right:
        #             temp=temp.right
        #         temp.right=cur.right
        #         cur.right=cur.left
        #         cur.left=None
        #     cur=cur.right
        
    #     ## recursive
    #     self.helper(root)
        
    # def helper(self, root):
    #     if not root:
    #         return None
    #     temp=root.right
    #     root.right=self.helper(root.left)
    #     root.left=None
    #     last=root.right
    #     if last:
    #         while last.right:
    #             last=last.right
    #         last.right = self.helper(temp)
    #     else:
    #         root.right = self.helper(temp)
    #     return root