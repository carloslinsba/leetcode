class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s = list(set(nums))
        nums.clear()
        nums += s
        nums.sort()
        return len(nums)

s = Solution()
#nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
print (s.removeDuplicates(nums))
print (nums)

        