class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        right = k-1
        count = 0
        for item in nums[:k]:
            count+=item
        left+=1
        right+=1
        maxcount=count
        while right<len(nums):
            count-=nums[left-1]
            count+=nums[right]
            if count > maxcount:
                maxcount=count
            left+=1
            right+=1
        return maxcount/k


#time complexity:O(n)
#space complexity: O(1) - constant
            
#done
