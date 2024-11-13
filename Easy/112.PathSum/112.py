# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:


    def hasPathSumHelper(self, root: Optional[TreeNode], targetSum: int,currentSum=0) -> bool:
        if root is None:
            return False
        currentSum+=root.val
        if (root.left or root.right):
            if self.hasPathSumHelper(root.left,currentSum):
                return True
            if self.hasPathSumHelper(root.right,currentSum):
                return True
        else:
            if (currentSum==targetSum):
                return True
            return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if (root.left or root.right):
            return self.hasPathSumHelper(root, targetSum)
        else:
            if root.val==targetSum:
                return True
            return False
        
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22
s= Solution()
s.hasPathSum(root,targetSum)


        
        