# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []

        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        
        curr = head
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != curr.val:
                return False
            curr = curr.next
        return True