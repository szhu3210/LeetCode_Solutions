# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## convert to list then sort (array can use cache which is much faster)
        last=head
        l=[]
        while last:
            l.append(last.val)
            last=last.next
        l.sort()
        res=ListNode(0)
        last=res
        for x in l:
            last.next=ListNode(x)
            last=last.next
        return res.next
        
        ## sort linked list (which is too slow due to the lack of cache performance)
        last=head
        res=ListNode(0)
        while last:
            t=last.next
            temp=res
            while temp.next and temp.next.val<last.val:
                temp=temp.next
            temp.next, last.next = last, temp.next
            last=t
        return res.next