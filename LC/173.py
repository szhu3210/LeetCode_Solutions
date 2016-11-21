# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    stack=[]
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root==None:
            return None
        self.stack=[root]
        while(self.stack[-1].left!=None):
            self.stack.append(self.stack[-1].left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.stack)>0 else False
        
    def next(self):
        """
        :rtype: int
        """
        res=self.stack.pop()
        if res.right!=None:
            self.stack.append(res.right)
            while(self.stack[-1].left!=None):
                self.stack.append(self.stack[-1].left)
        return res.val

        
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())