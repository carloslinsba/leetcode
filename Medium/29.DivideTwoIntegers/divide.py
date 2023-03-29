class Solution:
    
    def check_i(self, i:int)-> int:
        if i > pow(2,31) - 1:
            return pow(2,31)-1
        if i< -pow(2,31):
            return -pow(2,31)
        return i

    def perform_division(self, dividend:int, divisor:int)->int:
        i=0
        
        if divisor ==1:
            return dividend
        if divisor ==-1:
            return -dividend

        while (dividend>=divisor):
            dividend-= divisor
            i+=1
        return i

    
    def divide(self, dividend: int, divisor: int) -> int:
        
        if divisor ==0:
            return None

        if (dividend< 0 and divisor >0):
            quotient= -self.perform_division(-dividend, divisor)
            return self.check_i(quotient)

        if(dividend> 0 and divisor <0): 
            quotient= -self.perform_division(dividend, -divisor)
            return self.check_i(quotient)

        # -dividend/ dividend
        if (dividend< 0 and divisor <0):
            return self.perform_division(-dividend, -divisor)
            return self.check_i(quotient)
        
        #regular case
        quotient= self.perform_division(dividend, divisor)
        return self.check_i(quotient)
        
            
s= Solution()
dividend =2000000000
divisor = 1
print (s.divide(dividend, divisor))