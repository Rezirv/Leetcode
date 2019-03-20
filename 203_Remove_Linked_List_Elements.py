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
        last = ListNode(0)
        new = last
        while head:
            if head.val != val:
                new.next = ListNode(head.val)
                new = new.next
            head = head.next
        return last.next


