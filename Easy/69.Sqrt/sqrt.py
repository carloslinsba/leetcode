class Solution:
    def trying(self, x, try_number):
        if try_number*try_number == x:
            return try_number
        else:
            if try_number*try_number>x:
                return self.trying(x, try_number//2)
            else:
                if (try_number+1)*(try_number+1)>x: #if try_number*try_number <x and (try_number+1)*(try_number+1)>x:
                    return try_number
                return self.trying(x, try_number+1)
    def mySqrt(self, x: int) -> int:
        try_number = x//2
        return self.trying(x, try_number)

s = Solution()
input = 8
print (s.mySqrt(input))
                


