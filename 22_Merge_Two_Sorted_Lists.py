# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cache = []
        while l1:
            cache.append(l1.val)
            l1 = l1.next

        while l2:
            cache.append(l2.val)
            l2 = l2.next
        cache.sort()
        result = ListNode(0)
        l3 = result
        while cache:
            l3.next = ListNode(cache[0])
            l3 = l3.next
            cache.pop(0)
        return result.next

