# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(curr_node):
            if not curr_node or curr_node == p or curr_node == q:
                return curr_node

            left = self.lowestCommonAncestor(curr_node.left, p, q)
            right = self.lowestCommonAncestor(curr_node.right, p, q)

            if left and right:
                return curr_node

            return left if left else right

        return dfs(root)
