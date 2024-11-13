# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    newTree= TreeNode()

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        aux= root.left.copy
        root.left = root.right
        root.right = aux
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        

        