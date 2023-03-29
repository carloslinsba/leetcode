class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currentSum=0
        nums_list=[]
        for number in nums:
            currentSum+=number
            nums_list.append(currentSum)
        return nums_list
        

        