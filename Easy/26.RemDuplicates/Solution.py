class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        remove_list=[]
        for index,item in enumerate(nums):
            if index+1 <len(nums):
                if item == nums[index+1]:
                    remove_list.append(item)
        for num in remove_list:
            nums.remove(num)
        return len(nums)

nums= [0,0,1,1,1,2,2,3,3,4]
s= Solution()
s.removeDuplicates(nums)
print(nums)
