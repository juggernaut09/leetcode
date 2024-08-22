# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
            
        while head and head.val == val:
            head = head.next
        curr = head
        prev = None
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
                continue
            prev = curr
            curr = curr.next
        return head
