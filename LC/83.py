# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last=head
        while(last and last.next):
            if last.val==last.next.val:
                last.next=last.next.next
            else:
                last=last.next
        return head