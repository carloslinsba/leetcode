class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums= set(nums)
        nums = list(nums)
        nums.sort()
        try:
            positives_index= nums.index(1)
        except:
            return 1
        nums= nums[positives_index:]


        for index,item in enumerate(nums):
            if item !=index+1:
                return index+1

        
        # now index should match value


        return len(nums)+1
        
        #next interation/try should make bynary search

        
        


nums = [1,7,8,9,11,12]

s=Solution()
print ( s.firstMissingPositive(nums))