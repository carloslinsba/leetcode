class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        returnedLenght = len(nums)
        nextItem=None
        count=0
        numsRemoval=[]
        i=0
        for idx in range(len(nums)):            
            if i+1 < len(nums):
                nextItem = nums[i+1]
            else:
                nextItem = None
            item = nums[i]
            if item == nextItem:
                count+=1
                if count >1:
                    nums.remove(item)
                    i-=1
            else:
                count=0
            i+=1
        return len(nums)


s = Solution()
#nums = [1,1,1,2,2,3]
nums= [0,0,1,1,1,1,2,3,3]
print (s.removeDuplicates(nums))
print(nums)

      