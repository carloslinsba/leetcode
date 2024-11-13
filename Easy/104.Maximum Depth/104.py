# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi= 0
        
        def maxDepthHelper(root: Optional[TreeNode], count:int) -> int:
            nonlocal maxi
            if not root:
                return
            if not( root.left or root.right):
                if count>maxi:
                    maxi = count
                return
            maxDepthHelper(root.left, count+1)
            maxDepthHelper(root.right,count+1)

        maxDepthHelper(root, 1)
        return maxi
