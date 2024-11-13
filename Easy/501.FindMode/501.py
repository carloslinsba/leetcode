# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d=dict()
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.d = dict ()
        highestValue=0
        highestValues = list()

        self.findModeHelper(root)


        for key, value in self.d.items():
            if value == highestValue:
                highestValues.append(key)
            elif value > highestValue:
                highestValues = [key]
                highestValue = value
        
        return highestValues

    def findModeHelper(self, root:TreeNode) -> List[int]:
        val = root.val
        if self.d.get(val):
            self.d[val]+=1
        else:
            self.d[val]=1
        if root.left:
            self.findModeHelper(root.left)
        if root.right:
            self.findModeHelper(root.right)
