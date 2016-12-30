# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=0
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        # current tree is a univalue tree: 1. left is univalue 2. right is univalue 3. root has same value
        if not root:
            return None
        left = self.traverse(root.left) 
        right = self.traverse(root.right)
        if left==False or right==False:
            return False
        if left==None and right==None:
            self.res+=1
            return root.val
        if left!=None and right==None:
            if left==root.val:
                self.res+=1
                return root.val
            else:
                return False
        if left==None and right!=None:
            if right==root.val:
                self.res+=1
                return root.val
            else:
                return False
        if left==right==root.val:
            self.res+=1
            return root.val
        else:
            return False