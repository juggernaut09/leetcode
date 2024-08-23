# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2:
            if l1 and l2:
                sum = (l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                sum = (0 + l2.val + carry)
                l2 = l2.next
            elif not l2:
                sum = (l1.val + 0 + carry)
                l1 = l1.next
            carry =  sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy.next
        