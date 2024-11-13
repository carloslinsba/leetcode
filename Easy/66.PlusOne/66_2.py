class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l = len(digits)
        def plusOneHelper(i):
            nonlocal l
            if digits[l-1-i]<9:
                digits[l-1-i]+=1
                return digits
            else:
                if i==0:
                    digits.insert(0, 1)
                    l=len(digits)
                    digits[l-1-i]=0
                    return digits
                digits[l-1-i]=0
                return plusOneHelper(i=i+1)
        return plusOneHelper(0)
            
            

            
        