# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        result=[]

        def pathSumHelper(root: Optional[TreeNode], currentSum:int, nodes:list[int]= []):
            if not root:
                return
            nodes.append(root.val)
            currentSum+=root.val
            if not (root.left or root.right):#it is a leaf
                if currentSum==targetSum:
                    result.append(nodes)
            pathSumHelper(root.left, currentSum, nodes.copy())
            pathSumHelper(root.right, currentSum, nodes.copy())

        pathSumHelper(root, 0,[])
        return result



        
        