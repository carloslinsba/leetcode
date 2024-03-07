class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        s = sum(nums)
        if s<target:
            return 0
        min_len=len(nums)
        curr_idx=0
        r=len(nums)-1
        l=0
        for i in range(0, len(nums)):
            while s>=target:
                s-=nums[r]
                r-=1
                min_len=min(min_len, r-l+1)
            r+=1
            if r>=len(nums)-1:
                break
            s+=nums[r]
            while s>=target:
                s-=nums[l]
                l+=1
                min_len=min(min_len, r-l+1)
        return min_len


s = Solution()
#target = 11
#nums = [1,1,1,1,1,1,1,1]
target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))


                






            

