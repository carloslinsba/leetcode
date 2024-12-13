# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l=[]
        def sumNumbersHelper(root,s:str):
            if not root:
                return
            if not (root.right or root.left):
                l.append(int(s+str(root.val)))
            sumNumbersHelper(root.left,s+str(root.val))
            sumNumbersHelper(root.left,s+str(root.val))
        summ=0
        for item in l:
            summ+=item
        return item


        