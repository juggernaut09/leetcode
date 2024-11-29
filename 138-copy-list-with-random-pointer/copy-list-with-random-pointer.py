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
        A' -> B' -> C'

        A -> A' -> B -> B' -> C -> C'
        '''
        if not head:
            return head
            
        # creating new_nodes and merging with the existing nodes.
        curr = head
        while curr:
            dup_node = Node(curr.val, curr.next)
            curr.next = dup_node
            curr = dup_node.next

        # Setting random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next


        # Splitting the nodes
        original = head
        clone = original.next
        clone_head = clone

        while original:
            if original.next:
                original.next = original.next.next

            if clone.next:
                clone.next = clone.next.next

            original = original.next
            clone = clone.next

        return clone_head
        
            

        
             
