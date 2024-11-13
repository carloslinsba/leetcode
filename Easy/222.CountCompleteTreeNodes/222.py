# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=0
        def countNodesHelper(root):
            nonlocal count
            if not root:
                return
            count+=1
            countNodesHelper(root.left)
            countNodesHelper(root.right)
        countNodesHelper(root)
        return count
        
            