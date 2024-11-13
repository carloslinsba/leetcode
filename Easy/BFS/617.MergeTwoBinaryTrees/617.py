# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1:Optional[TreeNode], root2: Optional[TreeNode]):
            r = TreeNode()
            if not root1:
                r = root2
                return r
            if not root2:
                r = root1
                return r
            
            r.val = root1.val + root2.val
            r.left = merge(root1.left, root2.left)
            r.right = merge(root1.right, root2.right)
            return r
        return merge(root1, root2)


            
            
