class Solution:
    def minSubArrayLen_helper(self, nums: list[int], left, right)->bool:
        left+=1
        right+=1
        if left>=len(nums)-1 or right<=0:
            return True
        if nums[left]==nums[len(nums)-1-right]:
            return self.minSubArrayLen_helper(nums, left, right)
        if nums[left]<nums[len(nums)-1-right]:
            return True
        return False


    
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ssum= sum(nums)
        if ssum< target:
            return 0
        left=0
        right=0
        while ssum>=target:
            if nums[left]==nums[len(nums)-1-right]:
                if self.minSubArrayLen_helper:
                    ssum-=nums[left]
                    left+=1
                else:
                    ssum-=nums[len(nums)-1-right]
                    right+=1
                continue
            if nums[left]<nums[len(nums)-1-right]:
                ssum-=nums[left]
                left+=1
            else:
                ssum-=nums[len(nums)-1-right]
                right+=1
                
        return len(nums)-left-right+1
            



s = Solution()
target = 11
nums = [1,1,1,1,1,1,1,1]
print(s.minSubArrayLen(target, nums))


