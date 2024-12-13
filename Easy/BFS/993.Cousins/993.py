# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_depth=None
        y_depth=None
        x_parent =None
        y_parent=None
        def isCousinsHelper(root:Optional[TreeNode], depth:int, previous_root:Optional[TreeNode]):
            nonlocal x_depth, y_depth, x_parent, y_parent

            if not root:
                return
            if root.val==x:
                x_depth=depth
                x_parent=previous_root

            if root.val ==y:
                y_depth=depth
                y_parent=previous_root
            if x_depth and y_depth:
                return
            isCousinsHelper(root.left,depth+1, root )
            isCousinsHelper(root.right, depth+1, root)
        
        isCousinsHelper(root,0,None)

        if x_depth != y_depth:
            return False
        return True if x_parent != y_parent  else False 
            

#time complexity: O(n)
#space complexity: O(n)
