import re

class Solution:
    def removeNonAlpha(self, s:str)->str:
        return re.sub(r'[^a-zA-Z0-9]', '', s)

    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= self.removeNonAlpha(s)
        for i in range(0, int(len(s)/2) ):
            if s[i]!=s[ len(s)-1-i ]:
                return False
        return True

s= Solution()
input = "A man, a plan, a canal: Panama"
print( s.isPalindrome(input) )