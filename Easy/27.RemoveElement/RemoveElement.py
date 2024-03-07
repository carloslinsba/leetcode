class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort()
        right = len(nums)-1
        fromLeft = len(nums)-1
        fromRight = 0
        a = []
        for i in range(0, int ((len(nums)+1)/2)):
            if nums[i] == val and fromLeft ==len(nums)-1:
                fromLeft= i
            if nums[right]==val and fromRight ==0:
                fromRight =right
            right-=1
        a= nums[:fromLeft:]
        b= nums[fromRight+1::]
        nums= a+b
        return len(nums)

s =Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print (s.removeElement(nums, val))
print (nums)