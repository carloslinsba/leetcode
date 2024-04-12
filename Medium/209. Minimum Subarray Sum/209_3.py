class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum=0
        sum_l=0
        target_l=len(nums)+1
        if nums[0]==target:
            return 1
        
        for i in range(0, len(nums)):
            sum+=nums[i]
            sum_l+=1

            while sum>=target:
                if sum_l<target_l:
                    target_l=sum_l
                sum-=nums[i-(sum_l-1)]
                sum_l-=1

        if target_l>len(nums):
            return 0
       
        return target_l
        

target = 15
nums = [1,2,3,4,5]
s= Solution()
print(s.minSubArrayLen(target, nums))




                




