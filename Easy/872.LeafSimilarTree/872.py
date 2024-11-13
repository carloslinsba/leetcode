# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 =[]
        tree2=[]
        def dfs(root:Optional, l:list[int]):
            if not root:
                return
            if not (root.left or root.right): #isLeaf
                l.append(root.val)
            dfs(root.left,l)
            dfs(root.right,l)
        dfs(root1, tree1)
        dfs(root2, tree2)
        if len(tree1) != len(tree2):
            return False
        for i in range(len(tree1)):
            if tree1[i] != tree2[i]:
                return False
        return True
        




                

        