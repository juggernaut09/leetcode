# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        5
        '''
        # if not root.left and root.right:
        #     return root
        
        # left = self.isValidBST(root.left)
        # right = self.isValidBST(root.right)

        # if not left or not right:
        #     return False

        # if left.val < root.val <= right.val:
        #     return True
        # else:
        #     return False

        # return self.isValidBST()

        def dfs(node, lower = float("-inf"), upper = float("inf")):
            if not node:
                return True

            val = node.val

            if val <= lower or val >= upper:
                return False

            
            if not dfs(node.left, lower, val):
                return False

            
            if not dfs(node.right, val, upper):
                return False

            return True
            
        return dfs(root)

