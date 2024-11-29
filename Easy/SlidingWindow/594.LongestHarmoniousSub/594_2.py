class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()
        left=0
        right= left+1
        long=0
        while right<len(nums):
            if max (nums[left:right+1]) - min (nums[left:right+1]) ==1:
                if right - left>long:
                    long= right - left
                right+=1
            else:
                if max (nums[left:right+1]) - min (nums[left:right+1])>1: 
                    left+=1
                    if left==right:
                        right+=1
                else: 
                    right+=1

        return long +1 if long else 0



# nums=[1,3,2,2,5,2,3,7]
nums=[1,2,2,1]
print(Solution().findLHS(nums))

#done
