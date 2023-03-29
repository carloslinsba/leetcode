class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


s=Solution()
nums = [1]
target = 0

print ( s.search(nums, target) )