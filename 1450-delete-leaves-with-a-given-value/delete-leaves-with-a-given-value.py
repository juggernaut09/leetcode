# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root and root.val == target and not(root.left) and not(root.right):
            return None

        if root and not self.removeLeafNodes(root.left, target):
            root.left = None
        
        if root and not self.removeLeafNodes(root.right, target):
            root.right = None

        if root and root.val == target and not(root.left) and not(root.right):
            return None

        return root




        


