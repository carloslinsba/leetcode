class Solution:
    #incomplete
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return nums[0] # still needs formatting
        
        sequence=False
        
        for i,num in enumerate(nums):
            if i==0:
                continue
            if nums[i-1]==num:
                if not sequence:
                    sequence= True
                    print (num) # still needs formatting
                    #nums.
                continue
        
