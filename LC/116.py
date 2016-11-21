# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        temp=cur=root
        while cur.left:
            temp=cur
            while temp:
                temp.left.next=temp.right
                temp.right.next=temp.next.left if temp.next else None
                temp=temp.next
            cur=cur.left
        