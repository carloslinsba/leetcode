class Solution:
    
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        res = float('inf')
        s = 0
        
        for r in range(len(nums)):
            s += nums[r]
            
            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0


s = Solution()
#target = 11
#nums = [1,1,1,1,1,1,1,1]
target = 7
nums = [2,3,1,8,2,4,3]
print(s.minSubArrayLen(target, nums))