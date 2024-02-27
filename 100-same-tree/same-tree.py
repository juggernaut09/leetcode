# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        # BFS using queue
        p_que = collections.deque()
        q_que = collections.deque()

        p_que.append(p)
        q_que.append(q)

        while len(p_que) > 0 and len(q_que) > 0:
            node1 = p_que.popleft()
            node2 = q_que.popleft()

            if node1.val != node2.val:
                return False
            
            if node1.left != None and node2.left != None:
                p_que.append(node1.left)
                q_que.append(node2.left)
            elif node1.left != None or node2.left != None:
                return False

            if node1.right != None and node2.right != None:
                p_que.append(node1.right)
                q_que.append(node2.right)
            elif node1.right != None or node2.right != None:
                return False

        return True


        