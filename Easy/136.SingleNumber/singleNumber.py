class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for index,item in enumerate(nums):
            num= nums[index]
            nums.pop(index)
            if not num in nums:
                return num
            else:
                nums.insert(index, num)
s = Solution()
input = [1,0,1]
print(s.singleNumber(input))