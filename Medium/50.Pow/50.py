class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow=1
        neg = False
        if n<0:
            neg= True
            n=n*-1
        while(n>0):
            pow= pow*x
            n-=1
        if neg:
            return 1/pow
        return pow 

s =Solution()
x = 2
n=-2
print(s.myPow(x,n))