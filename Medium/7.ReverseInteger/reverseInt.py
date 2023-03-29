class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x<0:
            x=x*-1
            negative = True
        s= str(x)
        s=s[::-1]
        x= int(s)
        if x> pow(2,31):
            return 0
        return x if not negative else x*-1

s= Solution()
x= -123
print (s.reverse(x))


print(pow(2,31))