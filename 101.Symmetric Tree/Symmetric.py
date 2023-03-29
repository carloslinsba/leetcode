# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def inorderTraversal_helper_directed(self, root: TreeNode, list_inorder, direction) -> list[int]:
        if root is None:
            return []
        if direction == 'left':
            if root.left:
                self.inorderTraversal_helper(root.left, list_inorder)
            list_inorder.append(root.val)
            if root.right:
                self.inorderTraversal_helper(root.right, list_inorder)
        else:
            if root.right:
                self.inorderTraversal_helper(root.right, list_inorder)
            list_inorder.append(root.val)
            if root.left:
                self.inorderTraversal_helper(root.left, list_inorder)


    def inorderTraversal_directed(self, root: TreeNode, direction):
        list_inorder=[]
        self.inorderTraversal_helper_directed(root, list_inorder, direction)
        return list_inorder


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None:
            if root.right is None:
                return True
            else:
                return False
        left = self.inorderTraversal(root.left, 'left') 
        right= self.inorderTraversal(root.right, 'right')
        
        if len(left)!= len(right):
            return False
        else:
            for index, item in enumerate(left):
                if item != right[index]:
                    return False
        return True

        
        
s=Solution()
input = root = [1,None,2,3]
s.inorderTraversal(root)
        
