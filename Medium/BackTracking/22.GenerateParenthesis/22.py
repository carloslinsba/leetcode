class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtracking(i,left, right,  n, curStr):
            if i ==n*2:
                result.append(curStr)
                return 
            if left <n:
                backtracking(i+1, left+1, right, n, curStr=curStr+"(")
            if i <n*2:
                if right <left : 
                    backtracking(i+1, left, right+1, n, curStr=curStr+")")
                
        backtracking(0,0,0, n, "")
        return result



s = Solution()
s.generateParenthesis(2)

#done