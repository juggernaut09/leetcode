# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Create a dummyNode and set head as the dummy.next
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy


        # Move the prev to the node before the node which is at left position.
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the nodes between left and right using the same old technique.
        curr = prev.next
        prev1 = None
        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev1
            prev1 = curr
            curr = next

        # connect the reversed sublist with existing list.
        prev.next.next = curr
        prev.next = prev1


        return dummy.next 


        