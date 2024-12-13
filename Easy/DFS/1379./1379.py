# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def getTargetCopyHelper(root)->TreeNode:
            if not root:
                return None
            if root.val == target.val:
                return root
            v= getTargetCopyHelper(root.left)
            return v if v else getTargetCopyHelper(root.right)
        return getTargetCopyHelper(cloned)
            
            
#time complexity: On
#space complexity: On