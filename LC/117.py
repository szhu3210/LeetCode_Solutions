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
    
    def iterator(self, root):
        while root:
            if root.left:
                yield root.left
            if root.right:
                yield root.right
            root=root.next
            
    def connect(self, root):
        if not root:
            return
        cur=root
        while(cur):
            prev=None
            start=None
            for x in self.iterator(cur):
                if prev:
                    prev.next=x
                    prev=x
                else:
                    prev=x
                    start=x
            cur=start
        