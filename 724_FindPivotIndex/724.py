class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum=0
        rightSum=0
        for number in nums:
            rightSum+=number
        rightSum-=nums[0]
        if rightSum==0:
            return 0
        
        
        for i in range(1,len(nums)):
            leftSum+=nums[i-1]
            rightSum-=nums[i]
            if leftSum == rightSum:
                return i
        return -1


test={
    3 : [1,7,3,6,5,6],
    -1: [1,2,3],
    0 : [2,1,-1],
    5 : [-1,-1,0,1,1,0],
}
for entry in test:
    if entry == Solution().pivotIndex(test.get(entry)):
        print ('Success')
    else:
        print('Failed')
            


#for each index, we need to calculate two arrays.
#   the 0 until before the index
#   and the index +1 until the end of the index

# to speed things up, we might just calculate the whole array
# exclude the first index and see if it is equal to zero

# then we can sum (index-1) to the current array 
# and subtract the index from the whole array

            