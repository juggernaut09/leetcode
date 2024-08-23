"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head        

        #Interleaved List
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # random pointer
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Splitting
        original_head = head
        dup_head = head.next
        dup_head_cpy = dup_head

        while original_head:
            original_head.next = original_head.next.next
            dup_head_cpy.next = dup_head_cpy.next.next if dup_head_cpy.next else None
            original_head = original_head.next
            dup_head_cpy = dup_head_cpy.next

        return dup_head