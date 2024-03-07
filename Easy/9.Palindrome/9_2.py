import re 

class Solution:

    def removeNonAlpha(self, s:str)->str:
        return re.sub(r'[^a-zA-Z0-9]', '', s)


    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        if not s.isalpha():
            s= self.removeNonAlpha(s)
        
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

so = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(so))
