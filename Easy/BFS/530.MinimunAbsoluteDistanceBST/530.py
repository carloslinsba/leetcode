# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = list()

        def dfs(root:Optional):
            nonlocal l
            if not root:
                return
            l.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        l.sort()
        mini =pow(10,5)
        lastValue=mini
        for item in l:
            if abs(item - lastValue)<mini:
                mini = abs(item - lastValue)
            lastValue = item
            
        return mini


            



