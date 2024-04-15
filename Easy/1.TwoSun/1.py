class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums2=nums.copy()
        nums.sort()
        left=0
        right=len(nums)-1

        while(True):
            if left>right:
                return False
            if nums[left]+nums[right]>target:
                right-=1
                continue
            if nums[left]+nums[right]<target:
                left+=1
                continue
            left2= nums2.index(nums[left])
            right2= nums2.index(nums[right])
            if nums[left]==nums[right]:
                nums2.pop(left2) 
                right2= nums2.index(nums[right])+1
            return [left2,right2]

#nums = [2,7,11,15]
#target = 9
nums = [3,3]
target = 6 

s= Solution()
print(s.twoSum(nums,target))


