class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        
        nums.sort()
        max_cons=0
        curr_cons=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==0:
                continue
            if nums[i]-nums[i-1]==1:
                curr_cons+=1
                if curr_cons>max_cons:
                    max_cons=curr_cons
            else:
                curr_cons=0
        return max_cons+1

nums = [0,0]
s=Solution()
print(s.longestConsecutive(nums))




            

