class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits)<1:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        def letterCombinationsHelper(s:str, idx:int ):
            if idx==len(digits):
                result.append(s)
                return 
            for c in phone_map[digits[idx]]:
                letterCombinationsHelper(s+c,idx+1)
        letterCombinationsHelper("",0)
        return result

            
            

            
#done