# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ## Stack
        if not root: return []
        stack=[root]
        res=[]
        while stack:
            t=stack.pop()
            res.append(t.val)
            if t.right:
                stack.append(t.right)
            if t.left:
                stack.append(t.left)
        return res
        
        ## Morris Traversal
        res=[]
        cur=root
        while cur:
            if cur.left:
                temp=cur.left
                while temp.right and temp.right!=cur:
                    temp=temp.right
                if not temp.right:
                    temp.right=cur
                    res.append(cur.val)
                    cur=cur.left
                else:
                    temp.right=None
                    cur=cur.right
            else:
                res.append(cur.val)
                cur=cur.right
        return res