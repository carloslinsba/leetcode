class Solution:
    
    
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(i:int, curStr: str):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in phone_map[digits[i]]:
                backtrack(i+1, curStr + c)

        if not digits:
            return [] 
        
        backtrack(0, "")
        return res


s= Solution()
digits = "23"
s.letterCombinations(digits)
            

            
        
