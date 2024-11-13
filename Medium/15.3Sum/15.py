class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left=0
        right=len(nums)-1
        output = []
        while left<right:
            for middle in range(left+1, right):
                if nums[left]+nums[middle] +nums[right] == 0:
                    output.append([nums[left],nums[middle],nums[right]])
                if nums[left]+nums[middle] +nums[right] > 0:
                    break
            left+=1
        return output
