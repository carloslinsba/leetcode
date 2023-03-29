class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        d= dict()
        for item in nums:
            d[item] = item
        for i in range(0, len(nums)):
            if not d.get(i):
                return i
        return len(nums)


s=Solution()
nums = [3,0,1]
print (s.missingNumber(nums))