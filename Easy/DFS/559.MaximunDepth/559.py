"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

#we need to into each branch, 
# and get the max untill leaf
#which means we should increment some sort of counter, when going further.

class Solution:

    
    maxDepthNum = int
    def maxDepth(self, root: 'Node') -> int:
        self.maxDepthNum=0
        def maxDepthHelper(root:'Node', counter:int=0):
            if not root:
                return
            if self.maxDepthNum<counter:
                self.maxDepthNum=counter
            [maxDepthHelper(node, counter+1) for node in root.children]
        maxDepthHelper(root, 0+1)
        return self.maxDepthNum

#done

    
