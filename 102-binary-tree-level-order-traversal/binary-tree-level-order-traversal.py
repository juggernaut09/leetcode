# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # from collections import deque

        # if not root:
        #     return []

        # queue = deque([root])
        # res = []
        # while queue:
        #     level_order = []
        #     level_len = len(queue)
        #     for _ in range(level_len):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #         level_order.append(node.val)

        #     res.append(level_order)
                
        # return res


        result = []
        def dfs(node, depth):
            if not node:
                return 

            if depth == len(result):
                result.append([])

            result[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)


        dfs(root, 0)

        return result

            

