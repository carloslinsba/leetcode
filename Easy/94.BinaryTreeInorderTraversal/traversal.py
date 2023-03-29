# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    list_inorder=[]
    def inorderTraversal_helper(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        if root.left:
            self.inorderTraversal_helper(root.left)
        self.list_inorder.append(root.val)
        if root.right:
            self.inorderTraversal_helper(root.right)

    def inorderTraversal(self, root: TreeNode):
        self.inorderTraversal_helper(root)
        return list_inorder
        
        
s=Solution()
input = root = [1,None,2,3]
s.inorderTraversal(root)
        
