# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#for each node in root three, see if its value is the same as subroot
#if it is, see if the three is the same left-wise
#if it is, see if the three  is the same right-wise.abs

#naive solution, look for every single node.

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            if root.val == subRoot.val:
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

            return False
        
        def isSubtreeHelper(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                if not subRoot:
                    return True
                return False
            if not subRoot:
                return False
            if isSameTree(root, subRoot):
                return True
            
            return isSubtreeHelper(root.left, subRoot) or isSubtreeHelper(root.right, subRoot)
        
        return isSubtreeHelper(root, subRoot)

    
    
        

        
        