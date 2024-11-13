# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def dfs( root:Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            root.right= root
            root.left=None
        dfs(root)
        

        

#not done 
#tyred.

        