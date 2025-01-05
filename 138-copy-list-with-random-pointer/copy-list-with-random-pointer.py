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
        '''
        A -> B -> C
        A -> A' -> B -> B' -> C -> C'
        A' -> B' -> C'
        '''
        if not head:
            return head

        # Step 1 creating new nodes and linking with the existing list
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        # Setting random pointers
        curr = head
        while curr:
            if curr.random and curr.next:
                curr.next.random = curr.random.next
            if curr.next:
                curr = curr.next.next


        orig_head = head
        clone_head = head.next

        orig_curr = orig_head
        clone_curr = clone_head

        while orig_curr:
            if orig_curr.next:
                orig_curr.next = orig_curr.next.next
            if clone_curr.next:
                clone_curr.next = clone_curr.next.next
            orig_curr = orig_curr.next
            clone_curr = clone_curr.next

        return clone_head


        

            

        
             
