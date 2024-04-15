class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i=len(nums)-1
        while(True):
            new_target= target-nums[i]
            if new_target in nums:
                if nums.index(new_target)==i:
                    i-=1
                    continue
                return [nums.index(new_target),i]
            i-=1

s= Solution()
nums = [3,3]
target = 6
print(s.twoSum(nums, target))

        