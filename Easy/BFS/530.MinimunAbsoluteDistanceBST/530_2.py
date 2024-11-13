# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = list()

        def dfs(root:Optional):
            nonlocal l
            if not root:
                return
            heapq.heappush(l,root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        mini =pow(10,5)
        lastValue=mini
        
        while(l):
            item = heapq.heappop(l)
            if abs(item - lastValue)< mini:
                mini = abs(item - lastValue)
            lastValue = item
        return mini


            



