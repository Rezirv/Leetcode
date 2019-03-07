# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        new = ListNode(0)
        l = new
        j = list(set(a))
        j.sort(key=a.index)
        for i in j:
            l.next = ListNode(i)
            l = l.next
        return new.next

