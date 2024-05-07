# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev

        carry = 0
        curr = head
        while curr:
            num = curr.val * 2
            if carry:
                num = num + carry
            carry = 1 if num // 10 != 0 else 0
            curr.val = num % 10
            if not curr.next:
                if carry:
                    curr.next = ListNode(carry)
                    curr = curr.next
                    break
            curr = curr.next

        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev

        return head
        
            