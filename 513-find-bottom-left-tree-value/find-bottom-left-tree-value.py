# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''DFS Solution with Recursion'''
    def __init__(self):
        self.BottomLeftValue = None
        self.maxDepth = -1

    def dfs(self, root: Optional[TreeNode], currDepth: int):
        if not root:
            return
        if currDepth > self.maxDepth:
            self.maxDepth = currDepth
            self.BottomLeftValue = root.val
        self.dfs(root.left, currDepth + 1)
        self.dfs(root.right, currDepth + 1)    
        
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.BottomLeftValue



        