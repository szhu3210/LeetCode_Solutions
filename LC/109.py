# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        slow=dummy
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow.next
        root=TreeNode(mid.val)
        slow.next=None
        root.left=self.sortedListToBST(dummy.next)
        root.right=self.sortedListToBST(mid.next)
        return root