# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def solve(curr: Optional[TreeNode], isLeft: bool):
            if not curr:
                return 0
            if (not curr.left) and (not curr.right):
                if isLeft:
                    return curr.val
                else:
                    return 0
            
            left = solve(curr.left, True)
            right = solve(curr.right, False)

            return left + right

        return solve(root, False)
