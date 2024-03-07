class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = dict()
        for num in nums:
            if d.get(num):
                d[num]+=1
                if d.get(num)>1:
                    return True
            else:
                d[num]=1
        return False


s = Solution()
nums = [1,2,3,1]
print(s.containsDuplicate(nums))
