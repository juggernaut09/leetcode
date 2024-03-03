# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        target_index = count - n

        if target_index == 0:
            if head.next:
                head = head.next
            else:
                head = None
            return head
        else:
            i = 0
            prev = None
            curr = head
            while curr:
                if i == target_index:
                    prev.next = curr.next
                    return head
                prev = curr
                curr = curr.next
                i += 1
        return