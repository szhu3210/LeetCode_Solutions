# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        res1=ListNode(0)
        res1l=res1
        res2=ListNode(0)
        res2l=res2
        last=head
        while last:
            if last.val < x:
                res1l.next=last
                last=last.next
                res1l=res1l.next
                res1l.next=None
            else:
                res2l.next=last
                last=last.next
                res2l=res2l.next
                res2l.next=None
        res1l.next=res2.next
        return res1.next
        