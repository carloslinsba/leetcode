import re

class Solution:

    def clear_white_space(self, s:list[str])-> str:
        if len(s)<1:
                return ''
        while s[0] ==' ':
            s.pop(0)
            if len(s)<1:
                return ''
        return str(s)
    
    def isNegative (self, s:list[str])-> bool:
        if len(s)<1:
            return None
        if s[0]== '-':
            s.pop(0)
            return True 
        else:
            if s[0]== '+':
                s.pop(0)
        return False

    def myAtoi(self, s: str) -> int:
        lenght= len(s)
        if lenght<1:
            return 0
        x = re.search('\A *[+|-]?[0-9]+', s)
        if not x:
            return 0
        s = x.group()
        x2 = re.search('[+|-]?[0-9]+', s)
        if not x2:
            return 0
        num = int(s)
        if num< - pow(2, 31):
            return - pow(2, 31)
        if num >= pow(2, 31):
            return pow(2, 31) -1

        return num

s =Solution()
strs = " +-12"
print (s.myAtoi(strs))

