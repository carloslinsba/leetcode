class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result= []
        def combineHelper(current_number:int,l:list):
            if current_number > n:
                return
            l.append(current_number)
            if len(l) == k:
                result.append(l)
                return
            for num in range(current_number+1, n+1):
                combineHelper(current_number= num, l=l.copy())

        for num in range(1,n+1):
            combineHelper(num,[])
        return result
            
            
            
                
#done