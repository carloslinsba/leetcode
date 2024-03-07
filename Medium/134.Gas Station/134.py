class Solution:
    def canComplete(self, gas: list[int], cost: list[int], startIndex) -> bool:
        sum=0
        if gas[startIndex]<=cost[startIndex] and len(gas)>1:
            return False
        for i in range (0, len(gas)):
            if startIndex>=len(gas):
                startIndex=0
            sum+=gas[startIndex]
            if sum >= cost[startIndex]:
                sum-=cost[startIndex]
                startIndex+=1
                continue 
            else:
                return False
        return True

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        #naive approach
        startIndex=0
        for i in range (0, len(gas)):
            if self.canComplete(gas,cost,i):
                return i
        return -1

s=Solution()
#gas = [1,2,3,4,5]
#cost = [3,4,5,1,2]


#gas = [2,3,4]
#cost = [3,4,3]

gas = [2]
cost = [2]

print (s.canCompleteCircuit(gas,cost))
    # if end of list, then continue from zero

