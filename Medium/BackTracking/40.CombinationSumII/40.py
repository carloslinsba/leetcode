class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        if candidates[0] > target:
            return []

        def goright(summed:int, numbers:list[int], idx:int):
            if summed == target:
                result.append(numbers)
            if summed > target:
                return
            for i in range(idx, len(candidates) ):                
                goright(summed = summed+ candidates[i], numbers= numbers+ [candidates[i]], idx=idx+1)
        
        goright(0, [], 0)
        return result





candidates = [10,1,2,7,6,1,5] # 1,1,2,5,6,7,10
target = 8
s = Solution()
print(s.combinationSum2(candidates,target))


# not done
        