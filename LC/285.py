# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
        # find node address
        address=[root]
        while address[-1].val!=p.val:
            if p.val<address[-1].val:
                address.append(address[-1].left)
            else:
                address.append(address[-1].right)
        
        # if has right child go down to find
        if address[-1].right:
            cur=address[-1].right
            while cur.left:
                cur=cur.left
            return cur
        
        # if no right child, go up to find
        while len(address)>1:
            if address[-2].left==address[-1]:
                return address[-2]
            address.pop()
        return None