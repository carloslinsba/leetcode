class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        summ=0
        if len(nums)==0:
            return 0
        max_sub = nums[0]
        for item in nums:
            summ=max(item, summ+item)
            max_sub = max(max_sub, summ)
        
        return max_sub

#time complexity: O(n)
#space complexity: O (1)