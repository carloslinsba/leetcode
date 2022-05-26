class Solution(object):

    ROMAN_VALUE = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    MINUS_SUBSTRINGS = ["IV", "IX", "XL", "XC", "CD", "CM"]
    value_of_subtraction=0
    #value_to_ignore=0
    s=[]
    
    def regular_sum(self, s):
        sum =0
        for char in s:
            sum += self.ROMAN_VALUE.get(char)
            #print(sum)
        return sum

    def has_minus_substring(self,substring):
        if substring in self.s:
            self.value_of_subtraction += self.ROMAN_VALUE.get(substring[1]) - self.ROMAN_VALUE.get(substring[0])
            self.s = self.s.replace(substring, "")
            return self.has_minus_substring(substring)
        return
    
    def has_minus(self):
        for substring in self.MINUS_SUBSTRINGS:
            self.has_minus_substring(substring)

    def romanToInt(self, s):
        self.s = s
        self.has_minus()
        value_sum= self.regular_sum(self.s)
        value = value_sum + self.value_of_subtraction
        #print(value)
        return value
        

s = input("enter your roman number:\n").upper()
a = Solution()
print(a.romanToInt(s))