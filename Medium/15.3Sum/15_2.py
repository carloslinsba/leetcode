class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        k=0
        results = set()
        def threeSumHelper(j):
            for k in range(i+1,j):
                if nums[i]+nums[k]+nums[j] == 0:
                    if not [nums[i],nums[k],nums[j]] in results:
                        results.append([nums[i],nums[k],nums[j]])
                    threeSumHelper(j-1)
                if nums[i]+nums[k]+nums[j] > 0 and nums[k]>=0:
                    threeSumHelper(j-1)

        for i in range(len(nums)):
            threeSumHelper(len(nums)-1)
        return results