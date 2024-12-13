# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []
        if not root:
            return
        def flattenHelper(root):
            if not root:
                return
            l.append(root)
            flattenHelper(root.left)
            flattenHelper(root.right)
        
        flattenHelper(root)
        for i in range(0,len(l)):
            l[i].left=None
            l[i].right = l[i+1] if i+1<len(l) else None
        
#time complexity: O(n)
#space complexity: O(n)
            

