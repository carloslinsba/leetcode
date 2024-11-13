# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaf(self, root: Optional[TreeNode])->bool :
        return not (root.left or root.right)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.leaf(root):
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))

        
#done