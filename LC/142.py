# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f=s=dummy=ListNode(0)
        dummy.next=head
        if f and f.next:
            f=f.next.next
        else:
            return None
        s=s.next
        while f!=s:
            if f and f.next:
                f=f.next.next
            else:
                return None
            s=s.next
        a,b=dummy,s
        while a!=b:
            a=a.next
            b=b.next
        return a