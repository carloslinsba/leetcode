class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        results_list=list()
        if target in nums:
            results_list.append(nums.index(target))
            nums= nums[::-1]
            results_list.append( (len(nums) -1) - nums.index(target))
            return results_list
        return [-1,-1]


nums = []
target = 0

s= Solution()
print (s.searchRange(nums, target) )
