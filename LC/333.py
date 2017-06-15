# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root):
            # return True if the root is a BST, and num the number of max subtree found under root, and lo and high of this tree
            if not root:
                return (True, 0, None, None)
            l,r=find(root.left),find(root.right)
            if l[0] and r[0] and (l[3]<root.val if l[3] else True) and (root.val<r[2] if r[2] else True):
                return (True, l[1]+r[1]+1, l[2] if l[2] else root.val, r[3] if r[3] else root.val)
            else:
                return (False, max(l[1],r[1],1), None, None)
        return find(root)[1]
        