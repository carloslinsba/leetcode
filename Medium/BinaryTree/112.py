# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasPathSumHelper(root, sum)-> bool:
            if not root:
                return False
            c_sum=sum+ root.val
            if not (root.left or root.right) and c_sum==targetSum:
                return True
            return True if hasPathSumHelper(root.left, c_sum) else hasPathSumHelper(root.right,c_sum)
        return hasPathSumHelper(root,0)
            
#time complexity: O(n)
#space complexity: O(1)
