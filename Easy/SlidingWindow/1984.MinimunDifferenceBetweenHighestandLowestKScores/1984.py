class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        if len(nums)<k:
            return nums[len(nums)-1]-nums[0]
        min_score=nums[k-1]-nums[0]


        for i in range(1,len(nums)):
                if i+(k-1)>=len(nums):
                    break
                if nums[i+(k-1)]-nums[i]< min_score:
                    min_score=nums[i+(k-1)]-nums[i]
            
        return min_score

#time complexity: O(nlogn)
#space complexity: O(1)
#done