class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lenght= len(nums)
        for i in range(0,lenght):
            for j in range (i+1, lenght):
                if (nums[i] + nums[j] ==target):
                    return [i,j]

s = Solution()
input = [2,7,11,15]
target = 9
print (s.twoSum(input,target))
