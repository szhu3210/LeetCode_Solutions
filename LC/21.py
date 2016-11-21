# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode(0)
        last=res
        while(l1 or l2):
            if l1==None:
                last.next=l2
                return res.next
            if l2==None:
                last.next=l1
                return res.next
            if l1.val < l2.val:
                last.next=l1
                last=last.next
                l1=l1.next
            else:
                last.next=l2
                last=last.next
                l2=l2.next
        return res.next