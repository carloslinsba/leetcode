# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        heap = []
        item = None

        def getMinimumDifferenceHelper(root: Optional[TreeNode]):
            if not root:
                return
            heapq.heappush(heap, root.val)
            getMinimumDifferenceHelper(root.left)
            getMinimumDifferenceHelper(root.right)
        
        getMinimumDifferenceHelper(root)
        diff = pow(10, 5)
        value= heapq.heappop(heap)
        for i in range(len(heap)):
            value2 = heapq.heappop(heap)
            diff2 = abs(value - value2)
            if diff2< diff:
                diff= diff2
            value=value2
        return diff
            
            
