# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isLeaf(self,root: TreeNode)-> bool:
            return not (root.right or root.left)        

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, summ=0) -> bool:
        if not root:
            return False
        
        summ+=root.val
        if self.isLeaf(root):
            if summ==targetSum:
                return True        
        if self.hasPathSum(root.left, targetSum, summ) or self.hasPathSum(root.right, targetSum, summ):
            return True
        return False


#done
        
        


        
