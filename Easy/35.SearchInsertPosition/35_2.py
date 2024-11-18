class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        mini = 0
        maxi = len(nums)-1

        def searchInsertHelper(idx:int):
            nonlocal mini, maxi
            if nums[idx]==target:
                return idx
            if nums[idx]<target:
                mini=idx+1
            else:
                maxi=idx-1
            idx= mini + (maxi-mini)//2
            if mini>maxi:
                return  mini
            return searchInsertHelper(idx)

        idx= mini + (maxi-mini)//2
        return searchInsertHelper(idx)
        
            
nums = [1,3,5,6]
target = 2

#done