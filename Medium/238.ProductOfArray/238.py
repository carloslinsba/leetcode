class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product=[1]*len(nums)
        for i in range(1, len(nums)):
            left_product[i]=left_product[i-1]*nums[i-1]
        
        right_product=[1]*len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            right_product[i]=right_product[i+1]*nums[i+1]
            left_product[i]*=right_product[i]
        left_product[-1]*=right_product[-1]
        return left_product

s = Solution()
nums = [1,2,3,4]
#nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))

