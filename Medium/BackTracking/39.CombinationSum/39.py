class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        if candidates[0] >target:
            return []
        result= []    
        
        def goingleft(summed:int, numbers:list[int], idx):
            if summed > target or idx> len(candidates):
                return
            if summed == target:
                result.append(numbers)
                return
            
            for i in range(idx, len(candidates)):
                goingleft(summed + candidates[i], numbers + [candidates[i]], i) 
        

        goingleft(summed=0, numbers= [], idx=0)
                
        return result

        #done


# candidates = [2,3,6,7]
# target = 7
# candidates = [2,3,5] 
# target = 8
candidates = [3,5,8]
target =11
s= Solution()
print(s.combinationSum(candidates, target))

#This looks like :
# while summed < target:
#     continue adding - this needs to be recursive adding
# if equal:
#     result++
# if more:
#     return recursion branch

#    return one and try with next numbers.