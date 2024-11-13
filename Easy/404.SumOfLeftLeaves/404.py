# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isLeaf(self,root)->bool:
        return True if not (root.left or root.right) else False
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summ=0    
        
        def sumOfLeftLeavesHelper(root: Optional[TreeNode]) -> int:
            nonlocal summ
            if not root:
                return 0
            if root.left and self.isLeaf(root.left):
                summ+= root.left.val
            sumOfLeftLeavesHelper(root.left)
            sumOfLeftLeavesHelper(root.right)

        sumOfLeftLeavesHelper(root)
        return summ
        
        
        
#done

        