# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=ListNode(0)
        last=res
        last.next=head
        while(head and head.next):
            last.next=head.next
            head.next=head.next.next
            last.next.next=head
            last=head
            head=head.next
        return res.next