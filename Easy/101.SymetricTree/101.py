# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricHelper(self, root_left, root_right) ->bool:
        if root_left is None and root_right is None:
            return True
        if root_left is None or root_right is None:
            return False
        if root_left.val !=root_right.val:
            return False
        if self.isSymmetricHelper(root_left.left, root_right.right) is False:
            return False
        if self.isSymmetricHelper(root_left.right, root_right.left) is False:
            return False
        return True
            
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isSymmetricHelper(root.left, root.right)
            
        