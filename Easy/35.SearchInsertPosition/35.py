class Solution:
    
    
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        def searchHelper(i:int, nums2:list[int], mini, maxi):
            if nums[i]<target:
                i=maxi - (maxi-i) //2
                




        
        i = len(nums)//2
        mini=0
        maxi=len(nums)
        while True:
            item=nums[i]
            if item <target:
                mini=i
                i=maxi - (maxi-i) //2
                continue
            else:
                maxi= i
                i= i - (i-mini) //2

            return i
        return len(nums)
