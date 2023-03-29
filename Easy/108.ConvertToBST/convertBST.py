# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evenArray(self, nums:list[int])-> TreeNode:
        if len(nums)==0:
            return None
        
        rootIndex = int(len(nums)/2)
        if rootIndex>=1:
            root= TreeNode( nums[rootIndex], self.evenArray(nums[:rootIndex]), self.evenArray(nums[rootIndex+1:]))
        else:
            root= TreeNode( nums[rootIndex])
        print(root.val)
        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.evenArray(nums)
        

# Initialize list
nums = [50, 70, 30, 20, 90, 10, 50]
s=Solution()
s.sortedArrayToBST(nums)






    
