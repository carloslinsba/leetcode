# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i=0
        val=None
        def kthSmallestHelper(root):
            nonlocal i, val
            if val:
                return
            if root.left:
                kthSmallestHelper(root.left)
            i+=1
            if i==k:
                val = root.val
            if root.right:
                kthSmallestHelper(root.right)
        kthSmallestHelper(root)
        return val
            


