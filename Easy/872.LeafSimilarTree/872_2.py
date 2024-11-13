# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l =[]
        try:
            def dfs(root:Optional, insert: bool):
                nonlocal l
                if not root:
                    return
                if not (root.left or root.right): #isLeaf
                
                    if insert:
                        l.append(root.val)
                    else:                
                        v = l.pop(0)
                        if v!= root.val:
                            raise Exception()
                dfs(root.left,insert)
                dfs(root.right,insert)
            dfs(root1, True)
            dfs(root2, False)
        except:
            return False
        if l:
            return False
        return True

        




                

        