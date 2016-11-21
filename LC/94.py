# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # recursively
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
        # iteratively
        stack=[[root.left, root.val, root.right]] if root else []
        res=[]
        while stack:
            t=stack[-1]
            if t[0]:
                stack.append([t[0].left, t[0].val, t[0].right])
                t[0]=None
                continue
            if t[1]:
                res.append(t[1])
                t[1]=None
            if t[2]:
                stack.append([t[2].left, t[2].val, t[2].right])
                t[2]=None    
                continue
            stack.pop()
        return res
            