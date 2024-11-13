# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = list()
        def in_order(root: Optional[TreeNode], ) -> bool:
            if not root:
                return
            in_order(root.left)
            s.append(root.val)
            in_order(root.right)
        in_order(root)
        j=s[0]
        for i in range(1,len(s)):
            if s[i]<=j:
                return False
            j=s[i]
        return True
            
     

# done