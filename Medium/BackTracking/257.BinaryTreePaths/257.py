# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:    
        self.st = []
        stri = str(root.val) if root else ""
        self.binaryTreePathsHelper(root, stri)
        return self.st

    def binaryTreePathsHelper(self, root: Optional[TreeNode], stri) ->None:    
        if root.left:
            self.binaryTreePathsHelper(root.left, stri +"->"+str(root.left.val))
        if root.right:
            self.binaryTreePathsHelper(root.right, stri +"->"+str(root.right.val))
        if not (root.left or root.right):
            self.st.append(stri)
        return
        
        
#done