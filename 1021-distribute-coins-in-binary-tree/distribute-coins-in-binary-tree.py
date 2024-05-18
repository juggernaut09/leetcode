# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def solve(root, parent):
            if not root:
                return 0
            moves = solve(root.left, root) + solve(root.right, root)
            val = root.val - 1
            if parent:
                parent.val += val
            moves += abs(val)
            return moves
        
        return solve(root, None)

        