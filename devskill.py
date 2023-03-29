class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i=0
        responseArray=[]
        currentSum=0
        for number in nums:
            currentSum=currentSum+number
            responseArray.append(currentSum)
        return currentSum
            