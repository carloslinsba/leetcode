# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        h= []
        def minDiffInBSTHelper(root: Optional[TreeNode]):
            if not root:
                return
            heapq.heappush(h, root.val)
            minDiffInBSTHelper(root.left)
            minDiffInBSTHelper(root.right)
        
        minDiffInBSTHelper(root)
        v0= heapq.heappop(h)
        v1 = heapq.heappop(h)
        r = v1-v0
        v0=v1
        while(h):
            v1 = heapq.heappop(h)
            r=min(r,v1-v0)
            v0=v1
        return r

#time complexity: O(nlogn)
#space complexity: O(n)
