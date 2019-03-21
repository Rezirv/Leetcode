# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        else:
            new = ListNode(head.val)
            while head.next:
                head = head.next
                flag = ListNode(head.val)
                flag.next = new
                new = flag
            return new
