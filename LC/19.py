# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list=[]
        last=head
        while(last):
            list.append(last)
            last=last.next
        if n==len(list):
            return head.next
        if n==1:
            list[-2].next=None
            return head
        list[-n-1].next=list[-n+1]
        return head
        