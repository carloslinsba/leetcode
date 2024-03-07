class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        beginNums = nums[-k::]
        endNums = nums[:len(nums)-k:]
        nums.clear() 
        nums += beginNums+endNums

        """
        Do not return anything, modify nums in-place instead.
        """


s= Solution()
#nums = [1,2,3,4,5,6,7]
#k = 3
#nums = [-1,-100,3,99]
#k = 2
nums =[1,2]
k =5
s.rotate(nums, k)
print(nums)
