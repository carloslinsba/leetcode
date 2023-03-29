class Solution:
    def change(self, digits, toChangeIndex):
        if toChangeIndex==-1:        
            digits.insert(0, 1)
            return digits
        if digits[toChangeIndex]<9:
            digits[toChangeIndex]+=1
            return digits
        else:
            digits[toChangeIndex]=0
            return self.change(digits, toChangeIndex- 1)
    def plusOne(self, digits: list[int]) -> list[int]:
        toChangeIndex = len(digits)-1
        return self.change(digits,toChangeIndex)

            
digits = [9]
s = Solution()
print(s.plusOne(digits))