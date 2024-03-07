class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d = dict()
        i=0
        for item in range(len(nums)):
            if (d.get(nums[i])):
                d[nums[i]]+=1
                if d[nums[i]]>2:
                    nums.remove(nums[i])
                    i-=1
            else:
                d[nums[i]]=1
            i+=1
        return len(nums)


nums = [1,1,1,1]
s = Solution()
s.removeDuplicates(nums)