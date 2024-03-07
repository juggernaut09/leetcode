# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        target_idx = length//2
        result = []
        curr = head
        i = 0
        while curr:
            if i == target_idx:
                return curr
            i += 1
            curr = curr.next
        
        