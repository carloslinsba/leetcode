# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i=0
        value= None
        def in_order(root):
            nonlocal i, value
            if not root:
                return
            i+=1
            yield root.val
            
        
        while i!=k:
            value = in_order(root.left)
            if i==k:
                break
            value = in_order(root.right)
        return value

        
