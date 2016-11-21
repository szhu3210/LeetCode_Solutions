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
        res=ListNode(0)
        res.next=head
        last=res
        while last.next:
            probe=last.next
            depth=1
            while probe and probe.next and probe.val==probe.next.val:
                probe=probe.next
                depth+=1
            if depth>1:
                last.next=probe.next
            else:
                last=last.next
        return res.next