# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 0 Exception
        if not head:
            return True
        
        # 1 Find the middle using fast and slow pointers
        fast = slow = head
        fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        if not fast:
            l1, l2 = head, slow.next
            mid = slow
        else:
            l1, l2 = head, slow.next
            mid = slow
        
        # 2 Reverse the second half
        if not l2:
            return True
        rev = None
        last = l2
        while last:
            last.next, rev, last = rev, last, last.next
        l2 = rev
        
        # 3 Compare two list
        l10, l20 = l1, l2
        res = True
        while l2:
            if l1.val != l2.val:
                res = False
                break
            l1, l2 = l1.next, l2.next
        l1, l2 = l10, l20
        
        # 4 Restore/reverse the second half
        rev = None
        last = l2
        while last:
            last.next, rev, last = rev, last, last.next
        l2 = rev
        
        # 5 Combine l1, l2
        mid.next = l2
        return res