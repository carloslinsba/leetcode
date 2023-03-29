# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    currentDepth=1
    maxDepthNumber=0

    def isLeaf(self, node: TreeNode()):
            return 
            True if not (node.left or node.right) else False
    
    def calledInDepth(self, root):        
        if root.left:
            self.currentDepth+=1
            self.calledInDepth(root.left)
        if root.right:
            self.currentDepth+=1
            self.calledInDepth(root.right)
        
        if self.currentDepth > self.maxDepthNumber:
            self.maxDepthNumber= self.currentDepth
        currentDepth-=1
        

        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if self.isLeaf(root):
            return 1
        self.calledInDepth(root)
        return self.maxDepthNumber
        