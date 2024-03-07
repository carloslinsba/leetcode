class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num):
                return True
            else:
                d[num]=1
        return False

#nums = [1,2,3,1]
#nums = [1,2,3,4]
#nums = [1,1,1,3,3,4,3,2,4,2]
nums=[]

s = Solution()
print(s.containsDuplicate(nums))