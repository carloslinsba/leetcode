class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            if (target-nums[i] in nums):
                if (target-nums[i] == nums[i]):
                    n = nums[i]
                    nums.pop(i)
                    if (target-n not in nums):
                        nums.insert(i, n)
                        continue
                    return [i,nums.index(target-n)+1]
                return [i, nums.index(target-nums[i])]
            

            
        

s = Solution()
#nums = [2,7,11,15]
#nums = [3,2,4]
nums = [3,3]
target = 6
print (s.twoSum(nums, target) )