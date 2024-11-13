# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
        
    
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        s = set()
        def findTargetHelper(root: Optional[TreeNode], target: int) -> bool:
            if not root:
                return False
            if target-root.val in s:
                return True
            s.add(root.val)
            return findTargetHelper(root.left, target) or findTargetHelper(root.right, target)
            
        s.add(root.val)
        return findTargetHelper(root.left,target) or findTargetHelper(root.right,target)


#done