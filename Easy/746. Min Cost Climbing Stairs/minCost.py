class Solution:
    def CostClimbingStairs(self, init, cost:list[int])-> int:
        
        if len(cost)>2:
            costClimbOneStep =cost[len(cost)-1]
            costClimbTwoSteps=cost[len(cost)-2]
        else:
            if len(cost)==1:
                return cost[0]
            else:
                return cost [1] if cost[0]> cost[1] else cost [0]
        
        aux =False
        currentCost= cost[init]
        for i in range(init,0, -1):
            costClimbOneStep = cost [i-1]
            costClimbTwoSteps = cost [i-2]
            if i-1 <=0:
                break
            if aux:
                aux=False
                continue
            if costClimbTwoSteps <= costClimbOneStep:
                currentCost +=costClimbTwoSteps
                aux=True
            else:
                currentCost +=costClimbOneStep   
        return currentCost 
    
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost1= self.CostClimbingStairs(len(cost)-1, cost) 
        cost2= self.CostClimbingStairs(len(cost)-2, cost)
        return cost1 if cost1< cost2 else cost2
                    


s = Solution()
#cost = [10,15,20] #15
#cost = [1,100,1,1,1,100,1,1,100,1] #6
#cost=[0,2,2,1] #2
cost=[2,2,1,0] #2

print (s.minCostClimbingStairs(cost) )