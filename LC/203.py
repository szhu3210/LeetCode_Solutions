# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res=ListNode(0)
        res.next=head
        p = res
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return res.next