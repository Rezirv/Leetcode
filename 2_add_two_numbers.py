# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        l3 = result
        carry = 0
        while l1 and l2:
            var = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1.val = var
            l3.next = l1
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            var = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            l1.val = var
            l3.next = l1
            l3 = l3.next
            l1 = l1.next

        while l2:
            var = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l2.val = var
            l3.next = l2
            l3 = l3.next
            l2 = l2.next

        if carry:
            l3.next = ListNode(carry)

        return result.next




