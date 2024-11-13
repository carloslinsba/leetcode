# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidNode(self, root: Optional[TreeNode], number:int, left:bool) -> bool:
        if not root:
            return True
        if left:
            return root.val <number
        return root.val >number

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBSTHelper(root, mini, maxi):
            if not root:
                return True
            if root.val< mini:
                mini=root.val
            if root.val > maxi:
                maxi = root.val
            if not (self.isValidNode(root.left, mini, True) and self.isValidNode(root.right, maxi, False)):
                return False
            return isValidBSTHelper(root.left, mini, root.val) and isValidBSTHelper(root.right, mini, maxi)
        
        return isValidBSTHelper(root,root.val+1, root.val-1 )
        



            
#lacks the range.

        

        