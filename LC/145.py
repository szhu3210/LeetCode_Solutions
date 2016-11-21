# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## recursive
    #     self.res=[]
    #     self.tra(root)
    #     return self.res
        
    # def tra(self, root):
    #     if not root:
    #         return
    #     self.tra(root.left)
    #     self.tra(root.right)
    #     self.res.append(root.val)
        
        ## stack
        # revres=[]
        # stack=[root]
        # while stack:
        #     cur = stack.pop()
        #     if not cur:
        #         continue
        #     revres.append(cur.val)
        #     stack.append(cur.left)
        #     stack.append(cur.right)
        # return revres[::-1]
        
        ## Morris + reverse
        revres=[]
        cur=root
        while cur:
            if cur.right:
                temp=cur.right
                while temp.left and temp.left != cur:
                    temp=temp.left
                if not temp.left:
                    temp.left=cur
                    revres.append(cur.val)
                    cur=cur.right
                else:
                    temp.left=None
                    cur=cur.left
            else:
                revres.append(cur.val)
                cur=cur.left
        return revres[::-1]